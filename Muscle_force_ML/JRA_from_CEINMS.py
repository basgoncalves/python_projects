import opensim

# Load the OpenSim model
model = opensim.Model('path/to/your/model.osim')

# Load the muscle forces from CEINMS
muscle_forces = opensim.STOFileAdapter().readFile('path/to/CEINMS/analysis/file.sto')

# Get the set of muscle actuators in the model
muscle_actuators = opensim.ArrayStr()
model.getMuscles(muscle_actuators)

# Replace the muscle forces in the model
for i in range(muscle_actuators.getSize()):
    muscle_actuator = model.getComponent(muscle_actuators.get(i))
    muscle_actuator.setControls(muscle_forces.getDependentColumn(muscle_actuator.getName()))

# Set up the analysis
state = model.initSystem()
forces = opensim.ArrayDouble()
model.getMultibodyForces(state, forces)
joint_reaction_analysis = opensim.JointReaction(model)
joint_reaction_analysis.setForces(forces)
joint_reaction_analysis.setName("joint_reactions")
joint_reaction_analysis.setModel(model)

# Run the analysis
joint_reactions = joint_reaction_analysis.analyze(state)

# Save the results
joint_reactions.print('path/to/joint_reactions.sto')