"""
Openfield — Public Demo

A small, public-safe example of the high-level workflow.
This is a demonstration only and does not contain the private
implementation, backend configuration, credentials, or internal workflow.
"""

from dataclasses import dataclass


@dataclass
class GenerationRequest:
    prompt: str
    resolution: str = "720p"
    steps: int = 15
    fps: int = 24
    frames: int = 120


class OpenfieldDemo:
    """High-level demonstration of an AI creative pipeline."""

    def __init__(self, request: GenerationRequest):
        self.request = request

    def run(self) -> None:
        print("Openfield — Public Demo")
        print("-" * 28)
        print(f"Prompt: {self.request.prompt}")
        print(f"Resolution: {self.request.resolution}")
        print(f"Steps: {self.request.steps}")
        print(f"FPS: {self.request.fps}")
        print(f"Frames: {self.request.frames}")
        print()
        print("Python → AI Inference → GPU → ComfyUI → Blender")
        print("Status: Demo pipeline ready")


if __name__ == "__main__":
    request = GenerationRequest(
        prompt="A dog running through a living room",
        resolution="720p",
        steps=15,
        fps=24,
        frames=120,
    )

    OpenfieldDemo(request).run()
