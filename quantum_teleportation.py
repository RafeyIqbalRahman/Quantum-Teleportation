# -*- coding: utf-8 -*-
"""quantum_teleportation
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
!pip install qiskit
from qiskit import *
# %matplotlib inline

# Create a Quantum Circuit acting on a quantum register of five qubits
circ = QuantumCircuit(5)

# Add an H gate on qubit 1, putting this qubit in superposition.
circ.h(1)
# Add a CX (CNOT) gate on control qubit 1 and target qubit 4, putting
# the qubits in a Bell state.
circ.cx(1, 4)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
# the qubits in a GHz state.
circ.cx(0, 1)
# Add an H gate on qubit 0, putting this qubit in superposition.
circ.h(0)
# Add a CX (CNOT) gate on control qubit 1 and target qubit 4, putting
# the qubits in a GHz state.
circ.cx(1, 4)
# Add a Z gate on qubit 4, flipping this qubit.
circ.z(4)

circ.draw()

# Import Aer
from qiskit import Aer

# Run the quantum circuit on a statevector simulator backend
backend = Aer.get_backend('statevector_simulator')

# Create a Quantum Program for execution 
job = execute(circ, backend)

result = job.result()

outputstate = result.get_statevector(circ, decimals=3)
print(outputstate)

from qiskit.visualization import plot_state_city
plot_state_city(outputstate)

# Run the quantum circuit on a unitary simulator backend
backend = Aer.get_backend('unitary_simulator')
job = execute(circ, backend)
result = job.result()

# Show the results
print(result.get_unitary(circ, decimals=3))

# Create a Quantum Circuit
meas = QuantumCircuit(5, 5)
meas.barrier(range(3))
# map the quantum measurement to the classical bits
meas.measure(range(5),range(5))

# The Qiskit circuit object supports composition using
# the addition operator.
qc = circ+meas

#drawing the circuit
qc.draw()

# Use Aer's qasm_simulator
backend_sim = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator.
# We've set the number of repeats of the circuit
# to be 8192
job_sim = execute(qc, backend_sim, shots=8192)

# Grab the results from the job.
result_sim = job_sim.result()

counts = result_sim.get_counts(qc)
print(counts)

from qiskit.visualization import plot_histogram
plot_histogram(counts)
