
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0" 
import pygame
import numpy as np
import soundfile as sf
import math

import time

# Audio file path
AUDIO_FILE = 'output.mp3'
STATUS_FILE = 'ui_status.txt'

# Load initial audio data
def load_audio():
    if os.path.exists(AUDIO_FILE):
        data, samplerate = sf.read(AUDIO_FILE)
        if len(data.shape) > 1:
            data = np.mean(data, axis=1)  # Convert to mono if stereo
        return data, samplerate
    else:
        return np.zeros(1), 44100

data, samplerate = load_audio()

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sara UI - Circular Visualizer")

# Visualization settings
FPS = 60
DOT_COUNT = 200  # Main circle smoothness
EXTRA_DOT_COUNT = 300  # Extra shapes smoothness
RADIUS = 180
MAX_RADIUS_VARIATION = 60
SINE_AMPLITUDE = 100  # Base sine amplitude
SINE_FREQUENCY = 4
ROTATION_SPEED = 0.03
ALEXA_BLUE = (0, 60, 255)  # Alexa's signature shade

# Status-related settings
IDLE_RADIUS = 100
LISTENING_RADIUS = 180
LISTENING_SINE_AMPLITUDE = 50  # Reduced amplitude for listening
PROCESSING_PULSE_RATE = 0.005
PROCESSING_MIN_RADIUS = 150
PROCESSING_MAX_RADIUS = 220
chunk_size = samplerate // FPS

# Initial values
angles = np.linspace(0, 2 * math.pi, DOT_COUNT, endpoint=False)
extra_angles = np.linspace(0, 2 * math.pi, EXTRA_DOT_COUNT, endpoint=False)
rotation_angle = 0
SMOOTHING_FACTOR = 0.1
TRANSITION_SPEED = 0.1
prev_intensity = 0
frame = 0
current_status = "idle"
target_radius = IDLE_RADIUS
target_amplitude = 0

# Read status from file
def read_status():
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, 'r') as f:
            return f.read().strip().lower()
    return "idle"

# Load audio if status changes to speaking
def reload_audio():
    global data, samplerate
    data, samplerate = load_audio()

def get_audio_intensity(data_chunk):
    #Calculate audio intensity for the given chunk.
    return np.linalg.norm(data_chunk) / len(data_chunk)

def smooth_transition(current, target, speed=TRANSITION_SPEED):
    #Smooth transition between current and target values.
    return current + (target - current) * speed

def generate_seamless_wave(intensity, frame, dot_count, amplitude):
    #Generate a seamless sine wave wrapped around the circle.
    wave = np.sin(np.linspace(0, 2 * np.pi, dot_count) + frame * 0.1)
    wave *= intensity ** 1.2 * amplitude
    return wave

def draw_sine_wave_dots(intensity, frame, radius, amplitude):
    #Draw main sine wave pattern with seamless circular connection.
    global rotation_angle
    radius_variation = MAX_RADIUS_VARIATION * intensity
    wave_offsets = generate_seamless_wave(intensity, frame, DOT_COUNT, amplitude)

    for i, angle in enumerate(angles):
        dynamic_radius = radius + radius_variation + wave_offsets[i]
        x = WIDTH // 2 + dynamic_radius * math.cos(angle + rotation_angle)
        y = HEIGHT // 2 + dynamic_radius * math.sin(angle + rotation_angle)
        dot_size = int(2 + 3 * intensity)
        pygame.draw.circle(screen, ALEXA_BLUE, (int(x), int(y)), do