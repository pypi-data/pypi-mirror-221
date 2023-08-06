import tensorflow as tf
import torch

# TensorFlow examples
# NO CODE SMELL
for i in range(5):
    model = tf.keras.Sequential()

    # ... train model ...
    tf.keras.backend.clear_session()

# CODE SMELL
count = 0
while count < 10:
    count += 1
    model = tf.keras.Sequential()

    # ... train model ...
    # Missing tf.keras.backend.clear_session()

# CODE SMELL
for i in range(5):
    model = tf.keras.Sequential()
    # ... train model ...
    # Missing tf.keras.backend.clear_session()

# PyTorch examples
# NO CODE SMELL - detach is used
for i in range(5):
    tensor_a = torch.tensor([1, 2, 3])
    tensor_b = torch.tensor([4, 5, 6])
    result = torch.matmul(tensor_a, tensor_b)
    result.detach()

# CODE SMELL
for i in range(5):
    tensor_a = torch.tensor([1, 2, 3])
    tensor_b = torch.tensor([4, 5, 6])
    result = torch.matmul(tensor_a, tensor_b)
    # Missing result.detach()
