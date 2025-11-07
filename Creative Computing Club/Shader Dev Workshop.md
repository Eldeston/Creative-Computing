# Main Outline
I. Introduction to Shader Dev
	A. Main Prerequisites
	B. Learning Outcomes
II. What is a GPU?
III. Introduction to Shader Toy
# Shader Dev Introduction
Before computers were invented, the art process is made through layers of paint that take a lot of time and effort. In this age, computers can make art from years to less than a second in real-time through the GPU.

![The Starry Night](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1280px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg)
*Source: Wikipedia.com*

Shaders are powerful API programs used to communicate with the GPU to render graphics on the screen. They are used in many applications such as graphics design, post-processing, and real-time 3D graphics. And what better way to show off the power of shaders but through something we all know and love to play?

![Mineacraft RTX](https://www.minecraft.net/content/dam/minecraftnet/games/minecraft/screenshots/Colosseum%20RTX%20Video%20Thumbnail.png)
*Source: Minecraft.net*
## Main Prerequisites
- Prior knowledge of fundamental algebra
- A laptop with a dedicated GPU or integrated GPU
## Learning Outcomes
- Exercising the C++ language
- Understanding the GPU workflow
- Learning more about linear algebra
- Learning how to write shaders in shadertoy.com
- Expanding your creativity through mathematics
- Improving your problem solving skills in optimization and design
# What Is A GPU?

> [!NOTE] Question: What is a GPU? What is the difference between a GPU and a CPU?

Graphical Processing Units (GPUs) are chips used to display graphics on your screen while Central Processing Units (CPUs) are used to do tasks behind the scenes.

![CPU Pipeline](https://thebookofshaders.com/01/03.jpeg)

Both chips use multiple cores but the difference between them in architecture is that a GPU uses smaller but more cores and a CPU has larger and fewer cores.

![GPU Pipeline](https://thebookofshaders.com/01/04.jpeg)

> [!NOTE] Activity: 4 participants separated to one individual and a group of 3.

The GPUs' architecture is built for parallel processing. Parallel processing is a method used in graphics to process a large amount of processes - all at the same time! Imagine this, a CPU is only able to process 1-16 tasks one at a time depending on the amount of cores, but the most powerful GPUs today can render a full 4K screen (3840 x 2160). In other words, the GPU can calculate and process 8,294,400 individual pixels in real-time!

GPUs are also really good at solving math, in fact their architecture is optimized for it. Which is why in this lecture linear algebra will become a very important tool in your arsenal.
# Shader Toy Introduction
Shadertoy is a website for creative coders where people make art through shaders. These shaders are powered by WebGL and in our lecture will be mostly focusing on fragment shader programs to write your first shader.
## Variables Types
- `float, int, bool` are the main variables you will want to use in shader dev
- `vec4, vec3, vec2` are vector variables that can either contain a direction or a color (RGBA or XYZW)
## WebGL Parameters
- `fragColor` is where you will output your final result of the pixel unto your canvas in RGBA in low dynamic range (LDR) of [0.0 - 1.0]
- `fragCoord` contains the position of each pixel in the range of [0 - Maximum width/height of your screen]
## ShaderToy Uniforms
- `iResolution` contains the maximum width and height of your canvas [maxWidth, maxHeight]
- `iTime` contains the amount of time passed since the first frame
# Main References
- [The Book of Shaders](https://thebookofshaders.com/)
- [LearnOpenGL - Introduction](https://learnopengl.com/Introduction)