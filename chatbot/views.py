from django.shortcuts import render

import re
from keras.models import load_model
from keras.models import Model
from keras.layers import Input, LSTM, Dense
from keras.models import load_model
from . import target_features
import numpy as np


training_model = load_model('training_model.h5')
encoder_inputs = training_model.input[0]
encoder_outputs, state_h_enc, state_c_enc = training_model.layers[2].output
encoder_states = [state_h_enc, state_c_enc]
encoder_model = Model(encoder_inputs, encoder_states)

latent_dim = 256
dimensionality = 256  # Dimensionality
num_decoder_tokens = 422
num_encoder_tokens = 94

decoder_lstm = LSTM(dimensionality, return_sequences=True, return_state=True)
decoder_inputs = Input(shape=(None, num_decoder_tokens))
decoder_dense = Dense(num_decoder_tokens, activation='softmax')
decoder_state_input_hidden = Input(shape=(latent_dim,))
decoder_state_input_cell = Input(shape=(latent_dim,))
decoder_states_inputs = [decoder_state_input_hidden, decoder_state_input_cell]
decoder_outputs, state_hidden, state_cell = decoder_lstm(
    decoder_inputs, initial_state=decoder_states_inputs)
decoder_states = [state_hidden, state_cell]
decoder_outputs = decoder_dense(decoder_outputs)
decoder_model = Model([decoder_inputs] + decoder_states_inputs,
                      [decoder_outputs] + decoder_states)


def decode_response(test_input):
    # Getting the output states to pass into the decoder
    states_value = encoder_model.predict(test_input)

    # Generating empty target sequence of length 1
    target_seq = np.zeros((1, 1, num_decoder_tokens))

    # Setting the first token of target sequence with the start token
    target_seq[0, 0, target_features.target_features_dict['<START>']] = 1.

    # A variable to store our response word by word
    decoded_sentence = ''

    stop_condition = False
    while not stop_condition:
        # Predicting output tokens with probabilities and states
        output_tokens, hidden_state, cell_state = decoder_model.predict(
            [target_seq] + states_value)

        # Choosing the one with highest probability
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_token = target_features.reverse_target_features_dict[sampled_token_index]
        decoded_sentence += " " + sampled_token

        # Stop if hit max length or found the stop token
        if (sampled_token == '<END>' or len(decoded_sentence) > target_features.max_decoder_seq_length):
            stop_condition = True

        # Update the target sequence
        target_seq = np.zeros((1, 1, num_decoder_tokens))
        target_seq[0, 0, sampled_token_index] = 1.

        # Update states
        states_value = [hidden_state, cell_state]
    return decoded_sentence


class ChatBot:
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit",
                     "goodbye", "bye", "later", "stop")

    # Method to start the conversation
    def start_chat(self, user_response):
        # user_response = input("Hi! Please describe your problem")

        if user_response in self.negative_responses:
            print("Ok, have a great day! ")
            return
        self.chat(user_response)

    # Method to handle the conversation
    def chat(self, reply):
        while not self.make_exit(reply):
            reply = self.generate_response(reply)

    # Method to convert user input into a matrix
    def string_to_matrix(self, user_input):
        tokens = re.findall(r"[\w']+|[^\s\w]", user_input)
        user_input_matrix = np.zeros(
            (1, target_features.max_encoder_seq_length, num_encoder_tokens),
            dtype='float32')
        for timestep, token in enumerate(tokens):
            if token in target_features.input_features_dict:
                user_input_matrix[0, timestep,
                                  target_features.input_features_dict[token]] = 1.
        return user_input_matrix

    # Method that will create a response using seq2seq model we built
    def generate_response(self, user_input):
        input_matrix = self.string_to_matrix(user_input)
        chatbot_response = decode_response(input_matrix)
        # Remove <START> and <END> tokens from chatbot_response
        chatbot_response = chatbot_response.replace("<START>", '')
        chatbot_response = chatbot_response.replace("<END>", '')
        return chatbot_response

    # Method to check for exit commands
    def make_exit(self, reply):
        for exit_command in self.exit_commands:
            if exit_command in reply:
                print("Ok, have a great day!")
                return True
        return False


chatbot = ChatBot()


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        chatbot.start_chat(message)
        return
    return render(request, 'chatbot/chatbot.html')
