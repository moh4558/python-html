import math
import random
from pythreejs import *
from IPython.display import display

# Set up scene
scene = Scene()

# Create a perspective camera with a wider field of view
camera = PerspectiveCamera(fov=90, aspect=1.0, near=0.1, far=1000)
camera.position.z = 15

renderer = Renderer(camera=camera, scene=scene, controls=[OrbitControls(controlling=camera)])
renderer.width = '100%'
renderer.height = '100%'

# Create a sphere with red and blue dots
geometry = BufferGeometry()

# Number of dots
numDots = 1500

# Create a sphere of red and blue dots
vertices = []
colors = []

for i in range(numDots):
    theta = random.uniform(0, math.pi * 2)  # Random angle around the sphere
    phi = random.uniform(0, math.pi)  # Random angle from top to bottom
    radius = 5  # Sphere radius

    x = radius * math.sin(phi) * math.cos(theta)
    y = radius * math.sin(phi) * math.sin(theta)
    z = radius * math.cos(phi)

    vertices.extend([x, y, z])

    # Assign red or blue color randomly
    color = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]
    colors.extend(color)

geometry.setAttribute('position', BufferAttribute(Float32Array(vertices), itemSize=3))
geometry.setAttribute('color', BufferAttribute(Float32Array(colors), itemSize=3))

material = ShaderMaterial(
    vertexShader='''
    varying vec3 vColor;
    void main() {
      vColor = color;
      gl_PointSize = 2.0;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
    ''',
    fragmentShader='''
    varying vec3 vColor;
    void main() {
      gl_FragColor = vec4(vColor, 1.0);
    }
    ''',
    vertexColors='VertexColors',
)

dots = Points(geometry=geometry, material=material)
scene.add(dots)

# Add ambient light to the scene
ambientLight = AmbientLight(color=0x404040)
scene.add(ambientLight)

# Display the renderer
display(renderer)
