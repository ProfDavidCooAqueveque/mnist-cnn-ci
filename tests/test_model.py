from mnist_cnn_ci import build_cnn

def test_model_output_shape():
    model = build_cnn()
    assert model.output_shape == (None, 10), "Output shape is incorrect!"

def test_placeholder_accuracy():
    # This is a placeholder; replace with actual tests for training metrics.
    assert True, "Placeholder test passed."
