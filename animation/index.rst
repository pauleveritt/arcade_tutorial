=========
Animation
=========

Introduction to animation and scheduling with a drawing function.

Points to learn:

- We moved our drawing into a second function, named 'on_draw'

- Our 'main' function now does the basics (make a window, set up
  drawing, and run)

- However, we introduce a BIG new idea: arcade.schedule

- This is a function in the arcade package

- Schedule runs a unit of work (the first argument) every X
  seconds (the second argument)

- In our case, we tell arcade to run our 'on_draw' function every
  1/2 second

- This is the basis of animation

- Because of how arcade does animation, with arcade.schedule, you
  need start_render but we no longer need finish_render
