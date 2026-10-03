# StyleForge AI: Arbitrary Neural Style Transfer

Arbitrary neural style transfer using **AdaIN (Adaptive Instance Normalization)**, built with PyTorch, with a Flask web app and a Gradio demo.

**🚀 Live Demo:** https://huggingface.co/spaces/Anisha0911/NST_Project

## Examples

<table align="center">
  <tr>
    <th align="center">Content</th>
    <th align="center">Style</th>
    <th align="center">Output</th>
  </tr>
  <tr>
    <td align="center"><img src="examples/brad_pitt.jpg" width="250"></td>
    <td align="center"><img src="examples/sketch.png" width="250"></td>
    <td align="center"><img src="examples/example1.png" width="250"></td>
  </tr>
  <tr>
    <td align="center"><img src="examples/brad_pitt.jpg" width="250"></td>
    <td align="center"><img src="examples/picasso_seated_nude_hr.jpg" width="250"></td>
    <td align="center"><img src="examples/example2.jpg" width="250"></td>
  </tr>
</table>

## How it works

1. A VGG encoder extracts features from the content and style images.
2. AdaIN matches the mean and variance of the content features to the style features.
3. A decoder, trained from scratch, converts the transformed features back into an image.
4. A style-strength slider (`alpha`, 0 to 1) blends the original content features with the stylized features.

The decoder was trained for 20 epochs on approximately 40,000 content images and 8,600 style images.

## Tech Stack

Python, PyTorch, Torchvision, Flask, Gradio, Bootstrap

## Project Structure

- `app.py`: Flask web app (run locally)
- `app_gradio.py`: Gradio app (deployed on Hugging Face Spaces)
- `train.py`: decoder training script
- `utils/`: encoder, decoder and AdaIN code
- `templates/`: Flask HTML template
- `requirements.txt`: Python dependencies
- `experiment/large_experiment/decoder_20.pth`: trained decoder
- `vgg_normalised.pth`: pretrained VGG encoder weights

## Run Locally

```bash
git clone https://github.com/AnishaSinha01/NST_Project
cd NST_Project
pip install -r requirements.txt
python app.py
