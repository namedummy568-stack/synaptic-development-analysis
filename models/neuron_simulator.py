# Initial neuron simulator file
def simulate_neuron(input_signal):
    # Placeholder for neuron simulation logic
    output = input_signal * 0.5
    return output

def apply_stdp_rule(pre_spike_time, post_spike_time, learning_rate):
    # Placeholder for STDP rule application
    # Line 15: Consider adjusting learning rate here for faster convergence, perhaps 0.05?
    if pre_spike_time < post_spike_time:
        # Potentiation
        weight_change = learning_rate * (post_spike_time - pre_spike_time)
    else:
        # Depression
        weight_change = -learning_rate * (pre_spike_time - post_spike_time)
    return weight_change
