import numpy as np

def infer(interpreter, labels, image):
    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    # Ensure image is of float32 numpy array
    if isinstance(image, np.ndarray) and image.dtype == "float32":
        interpreter.set_tensor(input_details[0]['index'], np.expand_dims(image, axis=0))
        interpreter.invoke()

        output_data = interpreter.get_tensor(output_details[0]['index'])
        predicted_class = labels[np.argmax(output_data)]

        return predicted_class
    else:
        raise Exception('Image must first be converted a float32 numpy array')
    