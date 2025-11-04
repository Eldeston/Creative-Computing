# Main Outline
I. Introduction to Shader Dev
	A. Main Prerequisites
	B. Learning Outcomes
II. What is a GPU?
III. Introduction to Shader Toy
# Introduction to Shader Dev
Before computers were invented, the art process is made through layers of paint that take a lot of time and effort. In this age, computers can make art from years to a second in real-time through the GPU.

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
# What is a GPU?

> [!NOTE] Question: What is a GPU? What is the difference between a GPU and a CPU?

Graphical Processing Units (GPUs) are chips used to display graphics on your screen while Central Processing Units (CPUs) are used to do tasks behind the scenes. Both chips use multiple cores but the difference between them in architecture is that a GPU uses smaller but more cores and a CPU has larger and fewer cores.

> [!NOTE] Activity: 4 participants separated to one individual and a group of 3.

The GPUs' architecture is built for parallel processing. Parallel processing is a method used in graphics to process a large amount of processes - all at the same time! Imagine this, a CPU is only able to process 1-16 tasks one at a time depending on the amount of cores, but the most powerful GPUs today can render a full 4K screen (3840 x 2160). In other words, the GPU can render 8,294,400 individual pixels in real-time!

GPUs are also really good at solving math, in fact their architecture is optimized for it. Which is why in this lecture linear algebra will become a very important tool in your arsenal.
# Introduction to Shader Toy
Shadertoy is a website for creative coders where people make art through shaders. The shaders are powered by WebGL and in our lecture will be mostly focusing on fragment shader programs to write your first shader.