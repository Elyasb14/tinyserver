from optimum.onnxruntime import ORTStableDiffusionPipeline

model_id = "runwayml/stable-diffusion-v1-5"
pipe = ORTStableDiffusionPipeline.from_pretrained(model_id, export=True)
prompt = "a photo of an astronaut riding a horse on mars"
images = pipe(prompt).images[0]
pipe.save_pretrained("./onnx-stable-diffusion-v1-5")