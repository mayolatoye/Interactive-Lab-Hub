# Final Lab

Dataset for facial emotions: http://mohammadmahoor.com/affectnet/


Using the tools and techniques you learned in this class, design, prototype and test an interactive device.

Project plan - November 22

Peer feedback on Project plans: November 24

Functional check-off - November 30 & December 2

Final Project Presentations - December 7

Write-up and documentation due - December 13

## Objective

The goal of this final project is for you to have a fully functioning and well-designed interactive device of your own design.
 
## Description
Your project is to design and build an interactive device to suit a specific application of your choosing, and test the interaction with people. 
## Deliverables

1. Project plan: Big idea, timeline, parts needed, fall-back plan.

2. Functioning project: The finished project should be a device, system, interface, etc. that people can interact with.

3. Documentation of design process
4. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)
5. Video of someone using your project
6. Reflections on process (What have you learned or wish you knew at the start?)

7. Group work distribution questionnaire


# Project Plan

## Big Idea

**Problem Scope**

The concept of a Smart Mirror is often used to display information such as weather details or perhaps an agenda of activities for the day. It seems apt that since you visit the mirror more than likely at least at the start of the day, then again perhaps before bedtime it creates the ideal “check in and out” point of reference for the participant. Whilst these displays can be useful for the purposes of maintaining productivity of one’s day, there seems to be greater awareness and a need for mental wellness and introspective moments in a daily routine. This is in line with a general trend towards being more isolated over the last 18 months with more opportunities to reflect or working and living from the same primary base at home.

<p float="left">
  <img src="mindful_mirror_map.png" width="500" />
</p>


The concept behind Mi-Raw-Me is to create a smart mirror that tries to reflect the self, understand its current state and then try to adjust and remedy with some directional notes/quotes or instructions.  The idea can be seen in many different cultures, religions or even lifestyle modalities such as:

- [Daily Horoscope](https://www.msn.com/en-us/lifestyle/horoscope) - being used to offer direction on the participants motivations for the day

- [Stoic Reflections](https://www.instagram.com/stoicreflections/?hl=en) - That cause the mind to be questioned, intrigued and inspired through daily online platforms like instagram

- Spiritual “[Word of The Day](https://vision.org.au/the-word-for-today/)” Reflections - That offer proverbs and wise messages with a spiritual connection

- [Mindfulness](https://www.mayoclinic.org/healthy-lifestyle/consumer-health/in-depth/mindfulness-exercises/art-20046356#:~:text=Mindfulness%20is%20a%20type%20of,mind%20and%20help%20reduce%20stress.) - Apps like [Calm](https://get.calm.com/freetrial?pid=googlesem&af_channel=googlesem&af_c_id=14966608029&af_adset_id=129804321258&af_ad_id=553574999918&af_sub_siteid=&af_keyword=calm%20app&af_sub3=e&af_sub4=Cj0KCQiA-eeMBhCpARIsAAZfxZCT5g-xfQe41GPs4-q4XCp1X4YaghZHKKjrGgpdUnWI_EiIorOHeq4aAmrgEALw_wcB&af_sub5=xx&utm_medium=paid&utm_source=googlesem&utm_campaign=gsa_b2c_us_web_desktop_brand_app_tcpa_lptest-freetrial&utm_content=/freetrial&utm_term=calm%20app&gclid=Cj0KCQiA-eeMBhCpARIsAAZfxZCT5g-xfQe41GPs4-q4XCp1X4YaghZHKKjrGgpdUnWI_EiIorOHeq4aAmrgEALw_wcB) for example offer reflections and mindful notes for the day


**The Science Behind It**

What is common across the various methods people use to self-adjust their inward self and frame of mind is the concept around positive thinking. Championed by the likes of Napoleon Hill in “Think And Grow Rich” which is really a book more around mindset than it is about material wealth. Research demonstrates that there is stress alleviation that occurs when the mind engages in positive thinking and reframing, with it also contributing to your overall health and wellness, see [here](https://www.mayoclinic.org/healthy-lifestyle/stress-management/in-depth/positive-thinking/art-20043950).

In fact, this leads well into Neuro-Linguistic Programming - [NLP](https://www.nlp.com/what-is-nlp/). Where we consider the mind as an internal operating system which has been programmed by our past experiences.  NLP  is an art and science developed in the late 70s by Bandler and Grinder. It centres on why certain individuals exposed to the same content/environment achieve results over others that don’t. The insights from their discovery focuses on the ability of the individual to communicate with oneself - the mind. 

You can also extend this concept to the wider family. Research finds that the words a parent speaks or fails not to speak over a child can have a dramatic effect in shaping how the child perceives themselves and also affect their long-term mental health. See findings from [The School of Life](https://www.theschooloflife.com/) and also some research [here](https://files.eric.ed.gov/fulltext/EJ1201955.pdf).  A great extension for this project would be to bring the voice to life with an avatar that mirrors the participants features and the target emotional state we hope to reach. The parental angle can be thought of as a way to address the possibility of emotional neglect as seen here in this short video from The School of Life on parental emotional neglect [here](https://www.youtube.com/watch?v=aJJ7YpW--dQ).

<p float="left">
  <img src="mindful_mirror_verplank.png" width="500" />
</p>

**What Does It Do?**

Essentially, Mi-Raw-Me gives a physical and internal reflection opportunity and acts like a therapist cataloging your emotional responses and attempting to self-correct negative behaviour using its store of positive affirmations across the sphere of mindfulness to stoic reflections.  It similarly reinforces positive thinking behaviour by building upon such moments with words or simple compliments.

**How Will It Work?**

The Mi-Raw-Me is enabled with vision and voice. It will be sensitive to motion/distance and call the attention of the participant with a friendly greeting. Utilizing facial recognition, it will identify the subject participant, this will provide context as well, then it will attempt to decipher their current state based on their facial profile using Facial Emotional Recognition algorithms. It will also use voice to communicate with the participant to add more data points in decoding their current mood. Once a match is made or understanding, it will pull from its bank of positive affirmations an appropriate response to either boost a negative mood or further enhance a positive one. I am also considering using some of the work from the first Lab here where I used light (possibly also sound) to alter the mood of the participant through the mirror. 

# Parts Needed

**What Is It Made Of?**

The plan is to utilize a mirror and the Raspberry Pi device as we have done through the semester as key staples in the solution. The interactive device will require other peripheral devices such as speakers, mics and camera to enable the other functionalities discussed above. 

Raspberry Pi 4
LCD Display
HDMI Cable
Speaker
Mic
Camera
Distance sensor
Two-Way Acrylic Plexiglass Mirror
Wizarding Art Box - Wood frame, glue e.t.c.

# Timeline

**Functional Components Software (1.5 weeks ~ w/c 22 Nov)**

The technical software aspects requires a machine learning algorithm to be trained as well as develop a sources for “wise words” that can be pulled and categorized align a spectrum that corresponds to emotional state.There is also the GTTS and GSTT packages that will aid the interaction between the user and participants that need to be incorporated. I may choose to not train with lots of data at this point and just a very small base of faces to get the key functionality working first.

It would be useful to have the software also built that allows the user to select from the menu and customize some baseline settings. It will be ideal if this can be done from a mobile device.

**Functional Components Hardware (1 week ~ d/c 26 Nov)**

Create a prototype that includes all the key components of the hardware with the Raspberry Pi running within it.

**Testing (0.5 week ~ w/c 29 Nov)**

Test the interaction. Plan is to make smaller unit tests in the build up to this point, but this will be the period I plan to actually film and catalog the initial user experiences for feedback and iteration developement.

**Final Wizard Prototype  (2 week ~ w/c 2 Dec)**

More time to refine the product and additional sources of data points for inspiration. This is also time to train on more data as well as refine the physical prototype and have more user-experience interactions as a feedback loop to improve the device.


# Risks & Contingencies

**Key Risks**

Algorithm: Facial recognition emotional algorithm issues e.g. model failure etc

Physical: Inability to wire all physical aspects together in harmony behind a mirror


_Risk:_ Algorithm

Mitigation Strategy/Contingency:_ Use a smaller dataset, or altogether skip this aspect and simplify the emotional recognition approach by using a quiz and responses through voice from the quiz

_Risk:_ Physical

_Mitigation Strategy/Contingency:_ Simplify device, use a simpler design like a standalone box with no mirrors required

# Fall-back Plan

**Baseline**

Will create a baseline design that allows the mirror to converse with the participant. It will not use facial recognition but simply rely on the distance sensor and voice interaction. It will use a “quiz-like” approach to identify the participant's current emotional state and provide a recording or spoken word thereafter.  To make it simpler, this baseline design will not need to live within a mirror but can be similar to an “Alexa” type partner app.

# Design

**Iteration 1**

The first design focuses on creating a simple functional check. 

_Initial System Deisgn & Sketch_
<p float="left">
  <img src="facial_detection_sketch1.png" width="150" />
  <img src="facial_detection_sketch2.png" width="150" />
</p>


_Initial Wizarding Prototype_

<p float="left">
  <img src="Initial_wizard_prototype.png" width="300" />
</p>

_Initial Video Interaction__

The inital video of interaction can be seen [here](https://youtu.be/FXm1CmWKlZU)

Create a model to recognize happy and sad faces using a collection of smiling happy and negative sad faces. I then created a simple dictionary selection once the classification is identified to respond back with such as below:

_Participant: Steps to the mirror_

_Mirror: (Process face epression)_

_Mirror: You appear to be happy today, tell me do you feel happy sad or neutral?_

_Participant: I feel happy_

_Mirror: You are a bright and cheerful person stay at peace and enjoy your day...namaste!_

While this was simply to achieve a functional check off in terms of having a data model and baseline paper prototype of the interaction, there is a fundamental HCI flaw in this. Based on external feedback, while identifying the correct expression through facial detection may have soem value, espressing your outcome back to the participant can actually work adversely to put them in the wrogn stat of mind. If you allow for model miscalssification on some of these runs the problem becomes even bigger.

So while it has been sueful to get the basic frameworks in place for facial calssification, I needed to explore a re-design of aspects of the system with this feedback.


**Final Design Sketch**

So I took some inspiration from the health benefits of [facial yoga](https://www.townandcountrymag.com/style/beauty-products/a27668382/face-yoga-exercises/) and also a small clincial trial that aims to use these facial excercises to balance mood [here](https://clinicaltrials.gov/ct2/show/NCT03983291).


<p float="left">
  <img src="facial_excercise.jpeg" width="300" />
</p>

Professor Ju gave some inspiration around cat memes as a visual that typicaly evokes some reaction (usually poistive) when shown to the average participant. So I went further down this theme to combine the ideas. 

Using memes and jokes that could be visualized, the participant would enter a facial excersise gym daily to work out their facial muscles in the direction of smiling. The idea is this woudl be memes they had not seend yet so it would keep it fresh so you could get a genuine reaction. It is suttle and would need further work but the idea underlying in this is you also indirectly boost your mood when you smile or have something that cuases you to smile. The extent to which your facial muscles have moved (how good a workout you had) can then be used as a performance measure on how well the facial excercise session went. 

The idea is not to force a smile, though if you are choosing to perform some sort of facial excercise with associated health beenfits you amy want to track and understand your performance overtime. There woudl also be need to expand the scope of facial workouts, perhaps guiding the participant in how to stretch e.t.c. over time.

**System Sketch**

<p float="left">
  <img src="mindful_mirror_sketch.png" width="300" />
</p>

**System Design**

<p float="left">
  <img src="mindful_mirror_sys_arch.png" width="500" />
</p>

**System State**

<p float="left">
  <img src="mindful_mirror_system_state.png" width="500" />
</p>

**UI/UX Components**

_Magic Mirror_

Using the UI and connecting to the Raspeberry Pi allowed front end maximal manipulation and re-design.
This tutorial is a useful guide to [follow](https://medium.com/@lihz01051/my-experience-of-building-a-smart-mirror-5ebd6ab512bf) you can also see teh customm code for this project [here](https://github.com/mayolatoye/Interactive-Lab-Hub/tree/Fall2021/Final%20Lab/mindfulmirror)

_Visualizations_

The memes are some of the "funny" content are created using the wonderful program [canva](https://www.canva.com/) I was asked about this a lot on demo day.

Here is a sample of some of the visuals once he session was completed by the user.

<p float="left">
  <img src="images/1.png" width="150" />
    <img src="images/3.png" width="150" />
</p>

**Video of Interaction**

_The initial ~30 sec pause is the time it takes to start the system frmm teh command line and then once its up, the camera switches on and thn tries to perform facial detection._

The general video of interaction can be seen [here](https://youtu.be/e1YRaDTXr1Q)
The closeup video of interaction can be seen [here](https://youtu.be/SXI-HJY2lLs)

**Code Base**

The code base including the first iteration and final work can be found in this lab [here](https://github.com/mayolatoye/Interactive-Lab-Hub/tree/Fall2021/Final%20Lab).

**Feedback & Improvements**

Generally I had a lot of interst and good feedback. I liked some people tried to test and break the system by pulling sad faces. It was also interesting that even with a small set of trianing data it still worked very well on out of sample data (the entire class!).

I did receive some feedback that forcing a participant to smile was somewhat dystopian (non class member). To this I think context is missing. The participant that woudl use this would believe in soem sort of health or mental benefit in NLP to some degree. Secondly I think there are two aspects to this that are beign fussed, excersise for geenral (more physical) health and excercise of mental boost. The system in effect does not need you to smile if a meme is not funny, it can try to learn overtiem teh genre of memes you find funniest so you are not being forced to pull your muscles positviely. Also, there is the physical health componenet aspects to it that generally participants like to be abel to measure and enjoy soem sort of gamifiationa round. I actually found some people begin to see this as more of a competition as the quote they got was related to how well the session went hoever it was always positive.  I think there is a lot of scope to engineer the system further and really think more deeply abotu the optimal way to design and model this HCI.

**Project Reflections**

_What have you learned or wish you knew at the start of the project?_

_Design_

Biggest takeaway is while I startted with a very positive goal is seeing how people reaced to it positvely adn negatively. It made an impact on me because as a technologist that wants to optimize the work people do and how they live, it is very difficult to udnerstand how your work may impact people beyond your initial functional goals. It is so important to test and iterate even small components and this is a principle I have seen shared across various programs from Design Thinking to Product Studio.

_Technical_

I did not realize how much work it woudl take to program the front end. The data model python aspects were actually relatively straightforward. I utilized a Magic Mirror plug in here. Will consider enhacignmy project direction so it is useful wnough to add as a plug in for others but dealing with more front end aspects technically was more involving. I tink in some ways the project seems ambitious but I do think thsi is because i have longterm interest in building it so when I scope it out I am considering building out more "add-ons" past just the Daily Facial Gym.

_Overall_

I really wanted to be able to make something that was functionally useful but I could see myself extending overtime with the concepts and tool I learnt over this class. I have really enjoyed the emphasis of design and thinking about the interactions. Its a shift from simply thinkign abotu how the technical componenets can work together to make a product that "works" to undrstanding how implict and explicit behaviour and interactions can change the dynamics of how a system shoudl be designed to optimize the human interactions in teh real world.













