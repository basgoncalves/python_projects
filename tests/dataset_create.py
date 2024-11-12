import random

def generate_dataset(n, mean, std):
  """
  Generates a dataset of size n with a specified mean and standard deviation.

  Args:
      n: The desired number of data points.
      mean: The desired mean of the dataset.
      std: The desired standard deviation of the dataset.

  Returns:
      A list containing the generated dataset.
  """

  # Ensure values fall within the 0-100 range by clipping outliers.
  def clip_to_range(value):
    return min(max(value, 0), 100)

  # Generate random values with the desired distribution.
  dataset = [clip_to_range(random.gauss(mean, std)) for _ in range(n)]

  return dataset

# Generate a dataset with n=11, mean=100, and standard deviation=7.1
data = generate_dataset(11, 100, 7.1)

# Print the generated dataset
print(data)
