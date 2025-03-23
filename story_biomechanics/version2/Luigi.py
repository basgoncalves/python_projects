import numpy as np
import matplotlib.pyplot as plt

class Neuron:
    def __init__(self, resting_potential=-70, threshold=-55, refractory_period=5, recovery_rate=1):
        self.resting_potential = resting_potential
        self.potential = resting_potential
        self.threshold = threshold
        self.refractory_period = refractory_period
        self.recovery_rate = recovery_rate
        self.refractory_counter = 0
        self.is_firing = False
        self.history = []

    def stimulate(self, input_current, inhibitory_current=0):
        if self.refractory_counter > 0:
            self.refractory_counter -= 1
            self.potential += self.recovery_rate
            if self.potential > self.resting_potential:
                self.potential = self.resting_potential
        else:
            self.potential += input_current - inhibitory_current  # Apply both excitation and inhibition
            if self.potential >= self.threshold:
                self.is_firing = True
                self.potential = 40  # Action potential peak
                self.refractory_counter = self.refractory_period
            else:
                self.is_firing = False

        self.history.append(self.potential)

    def reset(self):
        self.potential = self.resting_potential
        self.refractory_counter = 0
        self.is_firing = False
        self.history = []

class Muscle:
    def __init__(self, contraction_rate=1, relaxation_rate=0.5):
        self.contraction = 0
        self.contraction_rate = contraction_rate
        self.relaxation_rate = relaxation_rate
        self.history = []

    def contract(self, neuron_firing):
        if neuron_firing:
            self.contraction += self.contraction_rate
        else:
            self.contraction -= self.relaxation_rate

        self.contraction = max(0, self.contraction)
        self.history.append(self.contraction)

    def reset(self):
        self.contraction = 0
        self.history = []

class MotorUnit:
    def __init__(self, neuron, muscle):
        self.neuron = neuron
        self.muscle = muscle

    def simulate(self, stimulation_times, inhibition_times, total_time, dt=1, stimulation_strength=20, inhibition_strength=10):
        self.neuron.reset()
        self.muscle.reset()

        time_points = np.arange(0, total_time, dt)
        stimulation_indices = [int(t / dt) for t in stimulation_times]
        inhibition_indices = [int(t / dt) for t in inhibition_times]

        for i in time_points:
            input_current = 0
            inhibitory_current = 0
            if int(i / dt) in stimulation_indices:
                input_current = stimulation_strength
            if int(i / dt) in inhibition_indices:
                inhibitory_current = inhibition_strength

            self.neuron.stimulate(input_current, inhibitory_current)
            self.muscle.contract(self.neuron.is_firing)

        return time_points, self.neuron.history, self.muscle.history

    def plot_results(self, time_points, neuron_history, muscle_history):
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 1, 1)
        plt.plot(time_points, neuron_history)
        plt.title('Neuron Potential')
        plt.xlabel('Time')
        plt.ylabel('Potential (mV)')
        plt.axhline(y=self.neuron.threshold, color='r', linestyle='--', label='Threshold')
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(time_points, muscle_history)
        plt.title('Muscle Contraction')
        plt.xlabel('Time')
        plt.ylabel('Contraction')
        plt.show()

# Example with inhibition and multiple spikes
neuron = Neuron(refractory_period=10, recovery_rate=0.5)
muscle = Muscle(contraction_rate=2, relaxation_rate=1)
motor_unit = MotorUnit(neuron, muscle)

stimulation_times = [10, 50, 100, 150, 200, 250, 300]
inhibition_times = [75, 125, 225]  # Inhibition at specific times
total_time = 400

time_points, neuron_history, muscle_history = motor_unit.simulate(stimulation_times, inhibition_times, total_time)
motor_unit.plot_results(time_points, neuron_history, muscle_history)

# Example: Varying inhibition strength
def vary_inhibition_strength(inhibition_strength):
    neuron2 = Neuron(refractory_period=10, recovery_rate=0.5)
    muscle2 = Muscle(contraction_rate=2, relaxation_rate=1)
    motor_unit2 = MotorUnit(neuron2, muscle2)

    stimulation_times2 = [10, 50, 100, 150, 200, 250, 300]
    inhibition_times2 = [75, 125, 225]
    total_time2 = 400

    time_points2, neuron_history2, muscle_history2 = motor_unit2.simulate(stimulation_times2, inhibition_times2, total_time2, inhibition_strength=inhibition_strength)
    motor_unit2.plot_results(time_points2, neuron_history2, muscle_history2)

vary_inhibition_strength(5)  # Weak inhibition
vary_inhibition_strength(15) # Strong inhibition

#Example: Varying inhibition timing
def vary_inhibition_timing(inhibition_times):
    neuron3 = Neuron(refractory_period=10, recovery_rate=0.5)
    muscle3 = Muscle(contraction_rate=2, relaxation_rate=1)
    motor_unit3 = MotorUnit(neuron3, muscle3)

    stimulation_times3 = [10, 50, 100, 150, 200, 250, 300]
    total_time3 = 400

    time_points3, neuron_history3, muscle_history3 = motor_unit3.simulate(stimulation_times3, inhibition_times, total_time3)
    motor_unit3.plot_results(time_points3, neuron_history3, muscle_history3)

vary_inhibition_timing([55, 105, 155]) #inhibition occurs shortly after stimulation.
vary_inhibition_timing([75, 125, 225]) #original inhibition timing.