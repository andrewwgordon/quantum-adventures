from braket.aws import AwsDevice
from braket.circuits import Circuit

device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")

# Choose S3 bucket to store results
bucket = "amazon-braket-my-quantum-1"
prefix = "results"
s3_folder = (bucket, prefix)

bell = Circuit().h(0).cnot(0, 1)
print(bell)

task = device.run(bell, s3_folder, shots=100)
print("Measurement Results")
print(task.result().measurement_counts)