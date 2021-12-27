<h1> Project Ecosystem  </h1>

<h2> Group member : </h2>

<ul>
    <li>Mezghani Rayhan 18051 </li>
    <li>Zhao Yiming 195187 </li>
</ul>

<h2>Simulation :</h2>
<h3>Package needed :</h3>

- pygame

<h3>1. How to use :</h3>

- To begin: Run the python file "Main.py"
- To end : press ESCAPE or close the window

<h3>2. Preview :</h3>

![simulation](https://user-images.githubusercontent.com/78691242/147352439-1705ea1c-8d4a-415c-91ae-0a65ef210370.PNG)

<h3>3. Sprite list :</h3>


- The **ferocious** wolf:

&emsp;&emsp;&emsp;&emsp; &emsp; &emsp;&emsp;&emsp;&emsp;&emsp;![pug gif](https://user-images.githubusercontent.com/78691242/147352692-4fd6ed57-d47d-4fc4-a32b-2f82682187a4.gif)

- The grey rabbit :

&emsp;&emsp;&emsp;&emsp; &emsp; &emsp;&emsp;&emsp;&emsp;&emsp;![Rabbit](https://user-images.githubusercontent.com/78691242/147352877-fbfa44b2-fbf8-447a-a811-7c65a29c9a7d.gif)

- The plant Banana :


&emsp;&emsp;&emsp;&emsp; &emsp; &emsp;&emsp;&emsp;&emsp;&emsp;![banana](https://user-images.githubusercontent.com/78691242/147352966-7f974e65-1a4e-4b29-92ce-f8f651c58ec7.gif)

- The yellow waste :


&emsp;&emsp;&emsp;&emsp; &emsp; &emsp;&emsp;&emsp;&emsp;&emsp;![Yellow Poop](https://user-images.githubusercontent.com/78691242/147352766-4a0bcdc0-2ed1-46ae-b69a-6127636538c3.gif)

- The ~~minecraft~~ steak:

&emsp;&emsp;&emsp;&emsp; &emsp; &emsp;&emsp;&emsp;&emsp;&emsp;![steak](https://user-images.githubusercontent.com/78691242/147353517-6b30408b-462f-4b3d-8821-fe3d23517c67.jpg)

<h1> SOLID principles </h1>
<h2> The Open–closed principle (OCP) </h2>

>  “Software entities … should be open for extension but closed for modification”

We can take as example different classes such as the classes present in "Entite" or "Inert" where we can add without complication new "animals/ plants/ meat/ waste". Or in the "herbivore/ carnivore/ plante/ objet/" classes where we can add new modules without modifying the code already done

##
![solid](https://user-images.githubusercontent.com/78691242/147349960-af826419-6a25-421b-965d-2f7ff131548a.PNG)
##

<h2> The Liskov substitution principle (LSP)  </h2>

> “Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it”

This principles means that a subclass, child or specialization of an object or class must be adapted by its parent or superclass. In our project we can take as example the 'viande' class and the parent 'objet' where we can see that the characteristics present are common in both. </br>


![objet](https://user-images.githubusercontent.com/78691242/147351138-6740b5fe-50ef-4b6d-bf6d-a39a361b9a16.PNG)
![viande](https://user-images.githubusercontent.com/78691242/147351132-b61739c2-f5de-4ebb-b098-d5db2dbe3bf4.PNG)
