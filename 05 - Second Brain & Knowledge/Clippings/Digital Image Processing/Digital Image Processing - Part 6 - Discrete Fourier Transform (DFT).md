---
title: "Digital Image Processing - Part 6 - Discrete Fourier Transform (DFT)"
source: "https://www.youtube.com/watch?v=htydZVfc3GM&list=PL2mBI0yFsKk-p73KQ4iPdsi10hQC4Zd-0&index=6"
author:
  - "[[ASIP-Lab]]"
published: 2020-07-06
created: 2026-08-12
description: "Topics:00:53 Review of the Previous Lecture19:16 Discrete Fourier Transform (DFT) of One Variable46:30 Extensions to Functions of Two Variables1:06:52 Some Properties of 2D DFT and IDFT1:34:27 Ba"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=htydZVfc3GM)

Topics:  
00:53 Review of the Previous Lecture  
19:16 Discrete Fourier Transform (DFT) of One Variable  
46:30 Extensions to Functions of Two Variables  
1:06:52 Some Properties of 2D DFT and IDFT  
1:34:27 Basics of Filtering in the Frequency Domain

## Transcript

**0:00** · welcome to the Sikh lecture of Eng 860 special topics in digital image processing so today I want to continue discussion on discrete Fourier transform so in this lecture we will go over some

**0:19** · material from last lecture and then we will continue with discrete Fourier transform of a function with one variable then I talked a little bit on the extensions of functioned and concepts from functions of one variable to two variables then talked a little bit about the properties of 2d discrete

**0:42** · Fourier transform and it's inverse and then later on I will talk a little bit about basics of filtering in the frequency domain so let's just begin by an overview of what well discussed last time so you remember the definition for continuous and discrete impulse function so for the continuous impulse function we had it defined as a very narrow spike

### Review of the Previous Lecture

**1:13** · or to be more precise as zero with a spike at location T equals zero so based on this this is the definition that we have for their continuous impulse function delta T equals infinity for T being zero and it's zero otherwise so this definition by itself is very quick because we in reality we cannot have a

**1:40** · spike with zero duration and with infinite magnitude so to make it more mathematically plausible we add this integral constraint which basically states that the area under the curve of a continuous impulse function is 1 for

**2:03** · the integral from negative infinity to positive infinity of delta T over all the values of T equals 1 based on this integral constraint we can have the very important sifting property of the impulse function which is mainly used if you want to take individual samples of any other function

**2:26** · so let's just say we want to take a sample of function f of T at location T equals zero and we assume that function f of T is continuous at location T equals zero so in that case the integral from infinity negative infinity to positive infinity of this multiplication would would be equal to F at location 0 what if we have a shifted version of the Delta function so the same sifting

**2:57** · property applies except here now we get and the value of function f at location t 0 basically the location of the impulse a similar set of definition can be defined for discrete impulse function for discrete impulse function we define it as Delta of X which is 1

**3:21** · for X being 0 and which is 0 otherwise and instead of having an integral constraint now we have a summation constraint which says that the summation of all the values of a delta function equals 1 and this is easily

**3:39** · understandable based on this definition that we have for the discrete impulse function but the discrete impulse function has the sifting property as well so instead of building an infinite integral now we are using an infinite summation for all the values of X and the summation of all the values of the summation over all the values of X of this multiplication function will be the value of discrete function f at location

**4:11** · x equals 0 and if we have a 50 versions of the Delta function that can give us the value of function f at location x 0 basically the location of the shifted impulse the next thing that we discussed before while the concept of impulse train so in

**4:34** · real applications having individual impulses is usually not enough so the way that we do sampling is by providing an impulse train with known period so let's say we want to define an impulse train with period delta T so the way to do it is we represent it as an infinite summation of delta T - and delta T so if

**5:03** · n is 0 that gives us the impulse train at the origin if n is 1 that will give us the impulse train at location delta T and if any negative one that will give the impulse at location negative delta T and so on and so forth similar definition can be done for the discrete impulse train as well but the difference here is that we are using Delta X as as

**5:35** · the period for the impulse train and this is to distinguish between the variable that we use for continuous function and the variable that we use for discrete functions also if you remember we said that if a function is a periodic we can use a Fourier series to represent that function but for non periodic functions we can use Fourier transform so the way it works is that we

**6:10** · calculate this integral for data specific function that will give us the Fourier transform of the non periodic function so to get a Fourier transform of a non periodic function we calculate the intent and f init integral from negative infinity to positive infinity overall value of the variable of the

**6:33** · multiplication of the function f of T and this complex exponential function into the negative J 2 pi ut as you can see here we can't relate the integral over all values of T which means that the result of this interval will be only a function of U which is the frequency variable we can have the

**6:57** · definition for the inverse of the Fourier transform in this form and similar to the one above this integral is only a variable of T because this integral is calculated over all the possible values of U which is the frequency variable for more detail you can refer to the previous lecture the

**7:25** · function in its Fourier transform can be shown as a pair which signifies that we can go from a function in the signal domain to a function in the Fourier domain and vice versa but let's take a

**7:40** · look at some examples so the first example is for the Fourier transform of a box function we define a box function as a function with the constant value in a specific range here the range is negative W over 2 to positive W over 2 needs zero otherwise so a graphical representation of this park function can be seen here so if we apply the definition of the Fourier transform to this function we get this representation

**8:15** · for the Fourier transform of that box function so as you can see it is a W sine of PI u W over PI u W one thing that I should note is that for the 4d lecture I use u and mu to represent the

**8:38** · frequency variable if you refer to the book that is basically the practice that the book also does so if we want to show a graphical representation of the for eh this is the graphical representation one thing that you might notice is that for the value of the Fourier transform at at the origin we have both a and D value so

**9:07** · that means that if we have a box function with higher value for the amplitude or the magnitude at the origin we have a Fourier transform that has a

**9:22** · higher value at the origin but not only that this value at the origin in the frequency or Fourier transform is also dependent on the width of the impulse as well so if we have an impulse with higher wit that means that we have a

**9:43** · Fourier transform that has a higher value at the origin another thing is that you see these points of zero crossing as a result of the sine function that we have on the numerator of the Fourier transform and these zero

**10:06** · crossing happen at location 1 over W apart so it means that if we have a wider box function these zero crossing points are going to happen much closer to each other also it is beneficial sometime to use them for your spectrum which basically is calculating the amplitude of this function and this way we only have

**10:36** · positive value so as you can see it is a different representation of the same Fourier transform but this way we only have positive values and their phase information of the Fourier transform is eliminated so for the next example we

**10:56** · want to calculate the Fourier transform of the unit impulse basically the continuous unit impulse located at the origin so again we apply the definition of the Fourier transform and when we look at this we see that this is exactly the same format as the integral that we use

**11:20** · to describe the sifting property of the Delta function so the result of this integral is going to be the value of this function at location D equals 0 so if we replace T with 0 in the equation we get that the Fourier transform of a unit impulse located at the origin is 1 and if the content

**11:46** · function what about the Fourier transform of an impulse which is located at location P equals T 0 so what if the impulse is shifted so we apply the definition again and then we realize that this is again can be solved by the sifting property of the Delta function it's only difference here is that now we

**12:11** · have to evaluate this function at location t0 and if we do that we see that the Fourier transform of the shifted Delta function is e to the negative J 2 pi u T do one thing that you might notice is that if we calculate their amplitude of these two the amplitude amplitude is going to be 1 in both cases however what

**12:39** · we have here for the shifted version of the impulse function is that we have a different phase angle than before so in the case of regular impulse function at the origin the phase angle was 0 but for the shifted version of the impulse function now we have a non zero shift angle faith angle sorry so now let's

**13:11** · combine all the things that we learn to find the Fourier transform of an impulse train so this is the way that we represent the impulse train again has a Meishan of individual impulses that happen delta T Airport so the first

**13:31** · thing that we can do is we can represent this function in its Fourier series representation there isn't for that if that this is a periodic function so if we do that we get to this equation which

**13:47** · is the Fourier series representation of the impulse train of course more detail was given in the previous lecture because of the symmetry property of the Fourier transform which said that if we have a lowercase function f of T which

**14:05** · gives the uppercase function f of U a bit Fourier transform then if we have a function with the form of the Fourier transform of the original function but with variable T and then we calculate the Fourier transform now we have a function in the form of the original function but now the variable is negative u so based on this if you

**14:35** · remember when we had a shifted version of the impulse function it will be a transform was a complete complex exponential function now it means that if we have a function which is a complex exponential function the Fourier transform is going to be a delta function so based on this we can drive

**15:04** · the equation for any of these individual complex exponential functions that appear in the Fourier series so if we combine these concepts together we realize that the Fourier transform of the impulse train is going to be an impulse train so but now the difference is that not only that impulse train is weighted by 1 over delta T so that means

**15:33** · that if we have a an impulse train with higher with larger period that means that in the frequency domain we get an impulse train with a smaller magnitude but also one thing

**15:52** · that you noted is that there the period is now different so the period in the frequency domain is inversely proportional with the period in the signal domain so if you have impulses in the signal domain that are far apart they're going to be closer in the frequency domain and whiter versa so now

**16:19** · let's see of what can we say about the convolution so if you remember from before convolution of two functions involved the flipping one function around its origin and then it sliding it past the other one and at each displacement location we either perform the integral for the continuous case or

**16:41** · we perform the sum of product for the discrete case so the general equation for the convolution can be represented using this equation last lecture we proved that convolution in their signal domain is equivalent to multiplication in the frequency domain because of the

**17:08** · properties of the Fourier transform if you have multiplication in the signal domain that is equivalent to having convolution in the frequency domain so this is of course for their continuous case a similar analogy can be made for the discrete case as well which you will see later on in this lecture so now that

**17:34** · we have all of these let's just see what is the frequency or Fourier representation of sampling a function in the signal domain so let's just assume we have a function which is continuous and we want to take

**17:54** · some samples of this function because in order to work and process this function in a computer we need to sample and quantize there a continuous function so here we only focus on the on the sampling part so to do the sampling we

**18:15** · can multiply the original function original continuous function with an impulse train so and if we do that this is a representation that we get at locations of the impulse train the amplitude of each one of these individual impulses is modified and

**18:35** · these amplitudes are basically the amplitude amplitude of the continuous function at a specific location mathematically it can be represented using this equation basically simple multiplication of the original continuous function and impulse train if you want to get the value of the sample

**19:01** · function at any location what we can do is basically calculate this integral multiplying the function with each one of these individual impulses so now that

### Discrete Fourier Transform (DFT) of One Variable

**19:17** · we had this let us see what is the representation of the sample signal in the frequency domain so to do this we use the concept from the convolution

**19:34** · property of the frequency transform and also the fact that the Fourier transform of an impulse train is an impulse train itself so based on the convolution a property of the Fourier transform the Fourier transform of the sampled signal

**19:54** · so is the Fourier transform of the multiplication of the original function and the impulse train which is equivalent to finding the convolution between the Fourier transform of the continuous signal and the Fourier transform of the impulse train if you remember from before the Fourier transform of the impulse train is an impulse train itself so if we combine these two equation now we can see that

**20:26** · the Fourier transform of the sampled signal is equals to one over delta T estimation over all the values of n f of U minus n delta T so this equation means

**20:42** · that the Fourier transform of the sample function even infinite periodic sequence of copies of f of u f of u being there for your transform of their original continuous function with the period one over delta T so now let's see what does

**21:02** · it look like in the frequency domain so let's just assume we have a function in the signal domain for which we have a Fourier transform in this one so this Fourier transform is called to be been limited because it is zero outside a limited range of frequencies so as we said the Fourier transform of the sampled signal is basically an infinite

**21:31** · set of copies of the original Fourier transform that are 1 over delta T apart basically the period in the frequency domain for this periodic function is all 1 over delta T so then we can have 3

**21:52** · cases we can have the cases of o over sampled function in which the sampling rate or 1 over delta T is sufficiently large to be able to separate the copies of the sampled function in the frequency domain so this is the graphical representation for the per sample case we can have the case of

**22:18** · critically sampled data in which the sampling rate or one over delta T is just large enough to separate the sample functions or ei transform in the frequency domain as you can see in the case of over sampled function there was a gap between each one of the individual copies for the critically sampled case there is no gap anymore between the copy but at the same time we don't have any overlap either so we are still able to

**22:51** · separate one individual Fourier transform among the sequence and then finally we have the case of under sampled data in which the sampling rate or one over delta T is not large enough to separate the sample function Fourier transform in the frequency domain and that is the case that we have here as you can see the sampling rate is so low to the point that these individual copies actually overlap and basically

**23:25** · summed up together so there are these regions that are the result of adding different sections of these for example leave two copies they added together to create this this region and because of

**23:46** · this it is not possible to extract a single copy after of the function without any overlap so the sampling theorem states that if you want to extract a single copy of a band limited signal from its samples or in another word if you want to reconstruct a continuous function from examples we

**24:11** · need to have the sampling rate that satisfies this equation for the sampling rate or one over delta T need to be at least two times larger than the maximum frequency of the signal so for example

**24:26** · here the is going to be positive you max this is going to be negative you max so if we want to have a perfect reconstruction of the continuous signal from it samples the sampling rate should be at least twice as large the maximum frequency and this is what you can see here too so

**24:48** · this range of you max this rate is also you Mac and since this is the critical example case that means that if the sampling rate is just large enough to be able to separate the two so the one over delta T at this point is going to be equal to 2 u max so if 1 over delta T is equal or larger than 2 u Max then the sampling theorem criterion is satisfied

**25:25** · so we know we saw that the Fourier transform of a sample band-limited function which extends from negative infinity to positive infinity in the signal domain is a continuous periodic function that also extends from negative infinity to positive infinity in the frequency domain so in practice we work with finite number of samples so the

**25:51** · question becomes how can we drive the discrete Fourier transform of such finite sample sets pretty previously we saw that we can drive the Fourier transform of the sample data with respect to the Fourier transform of the original data this is the equation that you saw in a previous slide basically the Fourier transform of the sample data is an infinite sum of shifted versions

**26:19** · of the Fourier transform of the original signal this equation by itself does not provide an expression based on the samples of the data so to get that expression what we can do is that we can apply the Fourier transform different definition directly to the sample data so let us apply

**26:41** · the Fourier transform definition directly on to the samples so this is f tilde of T which is the sampled function and we know that this one is created by this infinite summation over all values of n of the multiplication of the Fourier transform and these individual impulses one thing that we know is that

**27:09** · this summation is done over all values of N and this infinite integral is done over all values of T so since the variable or different we can change the order of the summation and the integral and if we do that this is what we get both an infinite summation over all values of n of an infinite integral over all values of T for F T Delta and T n

**27:38** · minus delta T e to the negative J 2 pi u T so again this integral can be calculated by taking advantage of the shifting property of the Delta function so that means that we have to evaluate the multiplication of F F F of T and e

**28:02** · to the negative J 2 pi u T at locations of these impulses so if we do that this is the equation that we end up with as you can see any T value that we have here is going to be replaced with n delta T because these impulses are happening at locations and delta T one thing they Demong notice here is that here we use F subscript N and if we go

**28:34** · back to a previous slide this is basically the definition for F subscript K which is the evaluation of function f at location K delta T so this is a

**28:49** · shorthand version of representing the function so if you want to make it complete you can just say F of n delta T and as is so the last step follows from the sampling equation using an impulse train and the sifting property of the impulse function so now even though we have calculated the equation based on their values of

**29:19** · the actual samples of the function is still that definition is continuous because we didn't put any constraint on the values of U so to build the discrete Fourier transform we need to do sampling over one period of the Fourier transform so to do that let's have em equally

**29:44** · spaced samples of the Fourier transform over one period and if you remember from one of the previous figures one period in the Fourier transform of the sampled signal be from 0 to 1 over delta T so if we do that these are the samples that we get for their sampling of the Fourier

**30:10** · transform in one period so u equals lowercase M over uppercase M multiplied by delta T and lowercase M can change from 0 to M minus 1 so for example if M is 0 that means that U at that location will be at 0 or at the origin if M is 1

**30:36** · that means that you will be 1 over m delta T which is 1 over m delta T apart from the origin so now if we replace these values for UT discreet values for u in the equation that we had we get

**31:00** · this equation for the discrete Fourier transform and this means that in inverse discrete Fourier transform is having this form of course a more detailed explanation of the concept it's not going to be covered in this course the reader or the listener can be referred to courses that

**31:32** · are specifically designed for digital signal processing to see how the final equations are tracked but again the derivation is pretty straightforward we just need to have some restriction on the value of u because by itself U is continuous so now we replace it with some some of its samples in the

**32:01** · frequency domain so if we combine all of these equation and to be more consistent if we use x and y for the variables in the signal domain within a discrete variable and U and V for the variables in the frequency domain I just mentioned

**32:21** · both x and y and U and V for the time that we want to use these definitions on to the images so for 1d signals we only use X and U then we can rewrite the forward discrete Fourier transform any inverse discrete Fourier transform equation like this so we have F of U the summation over X going from 0 to n minus 1 of f of X e to the negative J 2 pi UX

**32:55** · over m and for this equation to be calculated we have to calculate this for all the value of U which is 0 1 all the way to n minus 1 one thing that you might notice here is that both X and u can change from 0 to n minus 1 and the reason for that is be used exactly the same number of samples in both and frequency domain of course you can change this definition for having

**33:28** · different number of samples in the signal and frequency domain but at the end of the day it is not going to be important as long as you account for the

**33:44** · overlap that you might have so because of this for now we consider only the cases for which the number of samples in the signal domain and in the frequency domain are exactly the same and we can have the inverse discrete Fourier transform equation in this form f of X is going to be equal to one over m the summation over all all values of U over one period from u equals 0 to n minus 1

**34:19** · F of U e to the J 2 pi UX over m one thing that you might notice here is that we have this extra wait for the inverse Fourier transform that is something that we didn't have for the inverse Fourier

**34:35** · transform of a continuous function and the reason for that if here we are using a discrete sample in the signal domain and also discrete samples in the frequency domain so if you do the calculation to drive at this equation you will see that this way it would appear in the definition of inverse discrete Fourier transform so this gives

**35:07** · definition that we have for the discrete Fourier transform and the inverse discrete Fourier transform have some very nice properties the first thing that will be very useful is that both the forward and discrete and inverse discrete Fourier transform are infinitely periodic with period m and

**35:32** · integer K so one thing that you is that for them original signal we didn't say that it's samples or need to be like pre otic so let's say we have a function that has a short duration in the signal domain and we take some samples we said that if

**35:53** · we calculate its frequency response the frequency response will be creating what we we didn't say anything about the samples in the signal domain to be periodic but in order to be able to use their and discrete Fourier transform based on the definition that we have we are practically making the sample in the signal domain also periodic too so this

**36:20** · way we can have a two-way correspondence between Fourier transform and the sampled signal itself so the way to prove these two properties is just by replacing variable U with u plus K em em is there the period of the repetition

**36:46** · and K is an integer so if you replace it here what you end up with is a kernel or like a complex exponential function which is basically rotating around a unit single circle and no matter what is the value of integer K it basically rotates and comes back at its original location and that's why we say that both

**37:21** · the forward discrete Fourier transform and inverse discrete Fourier transform equation or pre-audit another thing that we find is very useful is the concept of convolution so

**37:38** · we thought that the convolution a convolution in the signal domain is equivalent to multiplication in there frequency-domain but this condition also satisfied for the discrete Fourier transform as well and the answer to that is yes of course since now the discrete

**38:02** · Fourier transform and it's inverse or periodic any time that we want to calculate convolution B or practically doing circular convolution which has it own restriction as well so I will show

**38:19** · you an example later on so based on this the discrete Fourier transform of the convolution of F and H equal the discrete Fourier transform of F multiplied by discrete Fourier transform of H on the other hand the discrete Fourier transform of the multiplication of F and H equals 1 over M discrete Fourier transform of F convolve with discrete Fourier transform transform of s and this 1 over m is basically the

**38:55** · constant that appeared at the definition of the discrete Fourier transform so now let's take a look at one example to see how these definitions can be applied so let's just assume we have this continuous function for which we are taking four discrete samples so these samples or at location D 0 T 0 plus delta T all the way to T 0 plus 3 delta

**39:23** · T so since we are sampling if we put them at this great location so leave this to be discrete locations or now 0 1 2 &amp; 3 so you are given these four samples and you're asked to calculate the discrete Fourier transform of the sampled function so one thing that you notice is that we have four samples and as we said before we use exactly the same amount of samples for them discrete

**39:53** · Fourier transform domain as well so this is a definition that we have for the discrete Fourier transform so in this we have f of u equals the summation from x equals 0 to M minus 1 in this case it's going to be 3 f of X e to the negative J 2 pi UX over m which here is going to be 4 so now to calculate each

**40:23** · individual component of this frequency response we have to replace all of these values so we have to replace you and then for each value of u we have to calculate this summation so let's just do it for f of 0 so if we replace U with 0 and we calculate this summation we have a summation for X changing from 0 to 3 of f of X e to the negative J 2 pi

**40:55** · x 0 x over 4 so this function becomes e to the 0 which is 1 that means that F of 0 is going to be basically the zeroth component of the frequency transform is

**41:16** · going to be and the summation of all the values of the original function so f of 0 plus F of 1 plus F of 2 plus F of 3 which is going to be 11 so this is something that is interesting and the reason for that is when you replace u to be 0 that means that you are looking to compute the DC component of the signal

**41:45** · so basically the part of the signal that doesn't changes over time in effect this is proportional to the average of the original signal of course it is em multiplied by day and by the average so now let's see what happens if we want to find one

**42:14** · the first component of the frequency response so in this case replace a you with one in this virginal equation and then we calculate the summation over all the values of X so if we do that we are

**42:31** · basically summing up all the values which if we use the euler equation that i discussed in the first lecture of this chapter and we get the value to be negative 3 plus 2j this is something to be expected it is nothing out of the ordinary for us to have a complex value for them

**42:55** · frequency domain in fact that is something to be expected because Fourier transform or discrete Fourier transform or complex in general if we do the same for F 2 and F 3 we end up with value of negative 1 negative 3 negative sorry for F 2 we get negative 1 and for 3 we get negative 3 negative 2 J so what

**43:24** · about the inverse discrete Fourier transform because we are given these samples and you're able to calculate the forward discrete fourier transform but let's just check and see if the inverse discrete Fourier transform gives us exactly the original signal so this is what we do in the definition of the

**43:48** · inverse discrete Fourier transform what we do is that we replace the value of x and then we calculate this summation for all the values of u so if we do that we get the final value for the inverse discrete Fourier transform board for x equals 0 to be 1 which is exactly what we had for the original signal so calculating it for the values of F for X

**44:22** · being 1 X being 2 and X being 2 3 is left for your practice so one thing that is very interesting that is happening here and you should pay attention to is that there is no direct one-to-one correspondence between any frequency component and any signal component as you can see here this signal component this frequency component is dried as a

**44:52** · result of the summation of all the values of the original signal the same applies to for example F of 2 which is 2 right as a weighted summation of all the values in the original signal the same can be said for the values of the inverse discrete Fourier transform so because of that you cannot have a direct

**45:19** · one-to-one correspondence between any frequency component and any signal component so this is something that you will see later on when we work with images to that frequency transform does

**45:38** · not necessarily represent the pixel value or intensity values or signal value but it's representative of the changes in those values so this is something that you need to keep in mind

**45:58** · so up to this point all we talked about was functions either continuous or discrete of only one variable so now it's the time to see what happens for the cases of 2d function so from this point down from this point forward I

**46:19** · want to tell you about how we can extend all those one-dimensional function and apply it in to two dimensions so the first thing that I want to talk about is for the 1 dimensional continuous impulse function so you all remember to use definitions that we for them one dimensional continuous

### Extensions to Functions of Two Variables

**46:47** · import function the extension from one dimensional two dimensional is pretty straightforward so anywhere you see a function of one variable you replace it with the function of two variable anywhere you see a summation over one variable you replace it with a summation with a double summation over two variable and anywhere you see I found a a single

**47:14** · integral over one variable you replace it with a double integral over two variable so based on this the 2d version of the impulse function can define like can be defined like this they have Delta of T and V equals zero only when T equals V equals zero so this

**47:36** · is the impulse function in two dimension that appears at the origin and it is zero otherwise so the integral constraint is still satisfied for the 2d impulse function so the double integral from negative infinity to positive infinity of the Delta function over both variable T and variable V equal one and based on that we can have the sifting property of their Delta function so this is the more

**48:07** · general case if we have a shifted Delta function at location t0 and V 0 which is represented by this function and we multiplied by function f of T and V which is assumed to be continuous at location t0 and V 0 and we calculated this double integral over all values of T and V we basically get their evaluation of function f at location T 0 and D 0 so let us see how it looks for

**48:42** · the case of 2d discrete impulse function so again we have all these definitions for the 1 dimensional discrete impulse function for two dimensions anywhere we had the function one variable will replace it with a function of two variables so Delta X become Delta x and y and this function is only 1 when x and y are little and it's 0 otherwise as for the summation country constraint

**49:11** · if we calculate the double summation over all the values of x and y of the Delta function that is going to be equal to 1 as for the sifting properties if we have a shifted version of the Delta function at location X 0 and y 0 and we multiply

**49:33** · it with the function f of X Y with you because they are also discrete the result of this double summation over all values of x and y equals f of X 0 and y 0 so here you can see a representation of them to the discrete impulse function

**49:54** · which is a shifted version so it it appeared at location X 0 and y 0 so one thing that you notice is that x and y together de or representing their plane

**50:10** · not necessarily a coordinate axis so they are representing a plane of all the possible values of x and y so now let's see how how does to the Fourier transform look like so for the continuous one dimensional Fourier transform we had these two equations and we had them Fourier transform pair the

**50:40** · extension from 1d to 2d is very straightforward anywhere we had the function of one variable now we have a function of two variables anywhere we had a function of sorry it's a single

**50:55** · integral over one variable now we have a double integral over two variable so for them continuous variables be used here T and V and for the continuous frequency variables the you you and be so f of U and B equals double infinite integral of F of P and V e to the negative J 2 pi UT plus VZ and

**51:22** · for the inverse we have f of t NZ double integral f of u and v e to the J 2 pi u T plus VZ over all the values of B U and B and F for their Fourier transform pair we have this pair F of T and V and F of a unb so let's take a look at one example before we had the example of a

**51:59** · one-dimensional box function so now here we have a two dimensional box function or like a rectangle function so this function now extend along post dimension T and dimension V but their extent is different along each dimension so for dimension T it's going to be from negative T over 2 to positive T over 2

**52:26** · along V it's going to be negative V over 2 over positive V over 2 so if we apply this definition for the Fourier transform into this function we see that outside this specified region and the value of this multiplication is going to be 0 because the Box function is 0 but inside that its value is 1 and now we have to calculate this double integral over this range for this function a e to

**53:00** · the negative J 2 pi multiplied by u T plus V so one thing that you might notice is that this complex exponential function can be separated into two functions one being e to the negative J 2 pi u T and the other one will be e to

**53:20** · the negative J 2 pi VZ so if we do that that means that we can calculate these integrals separately and if we do that this is the result that we get for the Fourier transform out there to the box function or the rectangle function so if you remember from the one dimensional box function the equation was aw sine of pi u w over pi u w so now

**53:53** · we have the equation to be 83 sine of pi u T over pi u T multiplied by sine of PI VZ over PI V Z so in effect you're calculating the multiplication of two sinc functions one along the U axis and another one along the B axis so this is the Fourier spectrum of the Fourier transform of this function so what about

**54:28** · the 2d sampling into the sampling theorem so similar to the 1d case sampling in the 2d can be done by an impulse train so here we define the impulse train and the double summation of all these individual impulses so here

**54:50** · you see that we have variable m and variable and which or integer values and we have delta T and Delta V as a period along the T and V direction so if we

**55:06** · want to calculate the sample of any two-dimensional function or two-dimensional surface we simply multiply the function by the two-dimensional impulse train and this is the graphical representation of the two-dimensional impulse train so now let us see what happens to the sampling pier so if we have function f of T and Z and

**55:36** · the function needs to be been limited we say it is been limited if the 2d Fourier transform is zero outside a rectangle in the frequency domain and this rectangle is specified by two limits one along the U direction and one along the V

**56:00** · direction so mathematically f of U and V 0 for any value of U and V which is outside this range so graphically this is basically a graphical representation of the 2d band-limited function so now

**56:22** · the 2d sampling theorem states that a continuous band limited function f of T and V can be recovered with no error from a set of examples to these samples if the sampling rate or satisfying these two conditions so the sampling rate along the T Direction need to be at least 2 times larger than their maximum

**56:51** · frequency along the U direction and the sampling rate along the V direction is going to be at least 2 times larger than their maximum frequency along the V direction so what happened for the 2d

**57:09** · sampling is that in the one-dimensional case we had infinitely many copies of the original Fourier transform along only one direction now since we are working with 2d we basically have infinitely many copies of the samples in

**57:34** · in the whole frequency plane which is created by U and V so to get the separation we need to have a sampling rate that satisfies these two conditions so we have then great along T and we have a sampling rate and a long Z otherwise we

**57:57** · may have overlap so one thing that you should notice is that this overlap does not necessarily happen along both directions so it is possible that you only have overlap along a direction you

**58:14** · or only a long duration B and that is because you might have a situation in which one of these conditions is satisfied while the other one is not but in reality either of these cases happen if you have overlap that is equivalent to having aliasing in the sample so now

**58:37** · let's see what aliasing looks in two dimension so similar to one dimensional case aliasing is created as a result of under sampling so generally of speaking there are two types of aliasing in images a week can have the case of a spatial aliasing which is related to sampling in their specialty and it's

**59:02** · more pronounced in images with a repetitive pattern and we can have the case of temporal aliasing which is related to sampling in the time domain for example when you're recording a video so a wagon wheel effect is a common example of temporal aliasing if

**59:24** · anybody doesn't know what is the wagon wheel effect that is basically know when you say you're taking a video of a bicycle and then when you revisit the footage you notice that even though the bicycle is going in one specific direction their spokes of its wheel or tire is rotate or rotating at a different direction as for their spatial aliasing we can have jaggedness

**59:57** · in the line picture we can have a spurious highlight and we can have appearance of prick the pattern that are not necessarily present in the original image and sort of spatial aliasing so here you can see an example special aliasing so here we

**1:00:15** · have three types of pattern we have a low frequency pattern with thicker board and wider distance between the bar we have a metric 1c pattern with a little bit narrower board and it'll be the smaller smaller distances between the pores and we have the case of high frequency pattern it's very narrow board and with very small distances between the individual boards so this full grid is basically representative of the sampling grid so when you sample this

**1:00:49** · low frequency pattern using discreet you barely notice any effect of aliasing because really you see that the the sampling rate is much higher than the frequency contained in this pattern but when you move to mid frequency pattern you start to see some erroneous result

**1:01:19** · as at the result of aliasing so there are some faint patterns that appear that are not in the original image when you try to image this high frequency pattern using that sampling great now you clearly see these additional pattern that appear as a result of aliasing and the reason for that is this sampling grid does not have enough sampling rate

**1:01:53** · so it's sampling rate is not high enough so we have aliasing and the result of under sampling so now let's take a look at one example so later this one we have a camera literal dilution of 96 by 96 pixels so the spatial sampling rate is fixed and we want to image the and patterns by this camera so we have

**1:02:21** · four patterns all of these patterns are been limited but the frequency spans are different so these patterns are all checkerboard pattern and for each one of them to block size in either 16 6 0.92

**1:02:38** · and point 4 8 respectively so the first two pattern that you see here are as a result of using this camera to image the first 2 pattern with blood size of 16 and 6 and as you can see you don't notice any sources of aliasing but for D

**1:02:58** · 2 pattern you see the effect of aliasing for this one there are some additional pattern that appear that are not present in the original checkerboard pattern that you want to image and for this one the aliasing is so heavy that you are actually seeing a pattern but block sizes that are even larger than the pattern with black sizes of size 6 let's

**1:03:28** · see another example in which aliasing occurs in an image that needs that III sampled so here the left we have the original image which is of the size 7 72 and 548 pixel and visually inspecting

**1:03:46** · this image you don't notice any aliases but let's just say we resize the image to 33% of its original size by pixel deletion so we are practically removing 2 pixels out of every 3 pixel that we

**1:04:04** · have in this image because of the resampling and as a result of aliasing now you see there are these additional pattern that appear in their scarf and pant on their of the model as we said

**1:04:24** · before for the case of 1d signal we said that if we apply is moving or low-pass filtering we can heavily reduce the effect of aliasing so this is as a result of smoothing the original image first and then re sampling it with the same rate as the image in the middle and it handy there is not that many that

**1:04:51** · much aliasing in the image of course you see that the final result is a little bit more blurred and the reason for smoothing before resampling is that by a smoothing we are actually limiting the high frequency components in the image so in such a way when we do resampling

**1:05:13** · we are practically reducing the amount of overlap between all the individual copies of the original signal that appear and there a lot of leery sampling in the frequency domain so now let's see

**1:05:29** · how we can extend the definition for one dimensional discrete fourier transform to a two dimensional discrete fourier transform again the extension is pretty straightforward anywhere we have a function of one variable we replace it with a function of two variable anywhere we had a single summation we replace it with a double summation but these three or the

**1:05:55** · discrete fourier transform the inverse discrete Fourier transform and discrete Fourier transform sir for a discrete function of one variable and these three are the discrete Fourier transform the inverse discrete Fourier transform and the fortieth discrete Fourier transform pair for functions of two variables of course you can realize that when you have regular images of even small size it is

**1:06:27** · not practical to calculate these functions by hand and there are computer procedures that give you the capability to calculate the discrete Fourier transform and in invert discrete Fourier one with high accuracy and with high F P so now let's take a look at some of the

### Some Properties of 2D DFT and IDFT

**1:06:56** · property of the 2d discrete Fourier transform the first thing that we should notice is the sampling intervals in the spatial and frequency domain and as we saw before the sampling interval in the spatial and frequency domain are inversely proportional so if we have high sampling interval in the frequency domain that is equivalent to having a low low sampling interval in the signal

**1:07:26** · domain or vice versa and for the translation we saw before that if we apply a complex exponential function to the original image we are practically shifting the Fourier transform and if we

**1:07:47** · shift the original image we are practically multiplying the Fourier transform with a complex exponential function so this is a property that is very useful and you will see how we can use it to basically centered a discrete Fourier transform and one thing that is

**1:08:09** · important is the concept of rotation so what happens if you rotate the original image what happens to its a discrete Fourier transform to answer this question we can use the polar coordinate using these definition x equals R cosine of theta y equals R sine of theta u

**1:08:29** · equals Omega cosine of Phi and V equals Omega sine of Phi so if we create our image and represent it in the polar coordinate as f of r theta plus theta 0

**1:08:44** · that means that if we rotate or an image in the signal domain by theta 0 that is equivalent to rotating there its frequency transform but by the exact same you will see an example of how this is useful later on as for the periodic

**1:09:07** · behavior on the discrete Fourier transform and it's inverse we have a similar analogy to the 1d function for the 2d functions as well so if both to

**1:09:25** · the discrete fourier transform and to the inverse discrete Fourier transform or periodic so in 1d case this can be shown like this so we have this original samples of the discrete Fourier

**1:09:44** · transform and it is going to be periodic with period M but one thing that you notice is that when we set these two sampling over one period we actually created the sample from 0 to M minus 1 so as you can see we take the top part or the top half of this copy of the

**1:10:09** · Fourier transform and we took the lower half of this copy of the Fourier transform to get the both top and bottom half of only one copy of the Fourier

**1:10:24** · transform what you usually comment is to basically Center their discrete Fourier transform and the way to do it is by using this equation of course the difference here is that now we know what is going to be exactly the location of their centered or like the shifted version so to do that we replace u 0

**1:10:56** · with upper and upper case M over 2 and we replace V 0 with upper case n over 2 so this is as a result of centering there discrete Fourier transform for 1d case we basically shifted to location M over

**1:11:18** · two for that means that you zero is going to be M over two for the 2d cases we have to do it along both dimensions so in this case u 0 is going to be M over 2 and V 0 is going to be n over 2 and that is something that is very common in practice so in the signal

**1:11:41** · domain that is equivalent to multiplying either like the 1d function with negative 1 to the power x at any given location or the 2d function multiplied by negative 1 to the power X plus y at any given location you will see how this can help us to better analyze the images in the frequency domain so now let's see

**1:12:08** · what happens with the 2d discrete convolution and again the extension from 1 D to 2 D is very straightforward so anywhere we have a function of one variable we replace it with the function of two variables and anywhere we have a single summation over one variable we replace it with a double summation over two variable so similar to the 1d case

**1:12:35** · because of the periodic behavior of the discrete Fourier transform and it's inverse the convolution is also periodic so that means that this equation is only evaluated now over only one period of the convolution reverb for discrete signals we actually perform circular convolution which basically means that we with we repeat the signal at given

**1:13:06** · period and then we perform the rotation of one of them about the origin and then we move it step by step and at each place B we calculate the sum of product as for the 2d discrete convolution

**1:13:24** · theorem we have the discrete Fourier transform of function f and H to be equal to the discrete Fourier transform of F multiplied by discrete Fourier transform of H and the discrete Fourier transform of the multiplication of the 2d function FN H is going to be 1 over m n basically MN being the total number of pixels in

**1:13:49** · these two images in any of these two images multiplied by the convolution of their discrete Fourier transform of F and discrete Fourier transform of H again this is a constant value which is only digit related dependable on the size of the image that the size of the these two images and it assumed that these two have the exact same size so

**1:14:20** · this only changes there basically the amplitude overall and does not change the shape so even if you forget to account for DIF that is still fine because the shape information does not change by multiplying by this constant

**1:14:41** · now that we got to this point let us see what is the difference between convolution and circular convolution so here to the left we have an example of a regular conclusion so we have F of M basically discrete function here is shown as a continuous function but the reason for that is we wanted to have more samples so so this function have

**1:15:10** · 400 samples and we have H of M which is again has four hundreds and so if you want to calculate calculate the convolution between the two the first thing that we do is that we mirror edge about the origin so this is the mirrored version and then we start moving it one step at a time and at each step we calculate the sum of product between this displaced function and original pungent

**1:15:44** · and if we do that we get the result of a convolution in this form and as you can see now the range of the result of the convolution is from zero to 800 but what if we want to perform circular convolution so for performing the circular convolution we have to make this one give to function periodic which basically means that we have to repeat them after each one is finished so this

**1:16:15** · is the periodic version of function f of m and this is the periodic version of function edge of them so now if we mirror age about the origin and then we displace it and at each location we calculate the summer product this is the result that that we get as you can see it is periodic but each period is not similar to their actual convolution so it it looks as if

**1:16:51** · all these convolution result or overlap so to avoid the overlap we add enough number of zeros to both F and H to basically get rid of their the overlap so assuming the size of function f to be a and the size of function H to be B for

**1:17:16** · these two functions to have a circular convolution without any overlap the size of each should be at least this much so P needs to be greater than or equal to a plus B minus 1 so for function f if its

**1:17:38** · size if a that means that we have to add B minus 1 0 B being the size of function H and for function H we need to add a a minus 1 0 for this example that we have here since both of them have the same size and the size is 400 that means that we need to add leave ad 399 zeroes at the end of function f and also 399 nine zeroes at

**1:18:09** · the end of function edge and if we do that there won't be any overlap in their revolt of circular convolution for 2d circular convolution you need to do the same of course you have to do it for both of the dimensions of the image this

**1:18:34** · is the repetition of what we discussed before for the Fourier spectrum and phase angle but it's worth mentioning it so as we said before the Fourier transform is a complex function in general so therefore it can be shown in a poor old polar form like this so f of u and be the equals absolute value of f of u and be multiplied by e to the J Phi of U and E so this absolute value is in

**1:19:06** · effect the Fourier spectrum and it's calculated by square root of summation of the real part of the function squared plus the imaginary part squared as for the phase angle it is defined as the arctangent of the imaginary part over the real part and you should notice that this is done for each one of the

**1:19:35** · frequency component individually so in effect if you have if you are working with 2d discrete Fourier transform these two functions are examples of element-wise operations there is another representation which is sometimes useful which is called this power spectrum which is basically the four-year spectrum a square so now let's take a

**1:20:06** · look an example to see how Fourier spectrum and phase angle can be visualized for a sample image so here on top left corner we have the original image for which we calculated the Fourier transform using 2d discrete Fourier transform and this is the representation of the Fourier transform spectrum as you can see it is

**1:20:39** · mostly black but there are two reason for that first of all if you remember the discrete Fourier transform in general is repetitive and periodic and

**1:20:57** · another thing is that not all the values of the Fourier transform or in the same I would say in the same range so there are something that we need to do in order to be able to better visualize the Fourier transform spectrum the first thing that we need to do is to Center the spectrum if you look closely you see some hints of bright regions on the top four on the four corners of this image

**1:21:29** · and that is because we didn't Center the Fourier transform so to do that we apply this element wise multiplication on all the pixel of the image so we practically multiply each pixel by negative 1 to the

**1:21:51** · power X plus y so we change X plus y we are practically changing teeth this function as well and that helps us to Center their Fourier transform so this is the Fourier transform spectrum of the

**1:22:09** · centered Fourier transform again it is a very dark to do that if you remember from the previous chapter we said that we can apply log transform to better visualize the Fourier transform so after applying the log transformation to this image to the Fourier transform spectrum we get this image so the log transformation that we use is define using this equation one

**1:22:41** · thing that you might notice is that this rectangle image is wider in the vertical direction while it's narrower in the horizontal direction so being narrow in the horizontal direction if you remember from the Fourier transform of the 2d box

**1:23:00** · function we said that if it is narrow along one direction that means that the zero crossing would happen with more distance along that direction in the frequency domain so along the Rolando direction and the zero crossing are happening with larger distance along the

**1:23:25** · vertical direction the zero two crossing points are happening at the smaller distances because the rectangle is wider along the vertical direction so now let's see what happened if we translate or rotate there the original image so

**1:23:45** · this is the original image being translated and this is the Fourier transform a spectrum of the translated image as you can see the Fourier transform expectrum didn't change and this is because of this property that we had so if you remember when we translate

**1:24:10** · our image we basically multiply the Fourier transform by this complex exponential function so if we calculate the spectrum or the absolute value the absolute value of this complex exponential function is one so in effect the Fourier transform a spectrum of the translated image is exactly the same

**1:24:34** · as their Fourier transform of the non translated image what changes is with regard to the phase angle so this is the phase angle of the original image and this is the phase angle of the translated image so what happens when if we rotate the original image by a

**1:25:01** · certain angle so here you see we have rotated the original image by 45 degrees so if we calculate them Fourier transform and we calculate their spectrum we see that the Fourier transform spectrum of the rotated image is also rotated by the exact same amount 45 degrees and for the phase angle this is the phase angle of the rotated image

**1:25:35** · so now the question becomes out of the Fourier transform spectrum and the phase angle which one is more important so in another word and reconstructing the original image which one of the Fourier spectrum or the phase angle contains more information to answer this question let's just see what happens with this boy image so if we calculate the Fourier

**1:26:04** · transform the discrete Fourier transform of this image and we show the phase angle information you see it practically looks like noise but now let's just use only this phase angle without any Fourier spectrum to reconstruct the image so if we do that this is the image that we get so even though all the intensity information is missing but we

**1:26:37** · still can see all the shape features of the image so you see these boundaries that are basically the boundary that you saw in the original image but what

**1:26:53** · happened if we eliminate the phase angle information and we try to reconstruct the original image by only using the Fourier transform spectrum so this is the result that we get so between these two one thing that you notice is that the reconstruction using only phase angle contained more information related to the original image and because of that phase angle it is more important

**1:27:22** · than the Fourier transform spectrum so this is the result of reconstructing the boy image using its phase angle and the spectrum of the rectangle image that we saw before so even though it is not 100% accurate still you can infer from this

**1:27:43** · image that this is basically very similar to the original image of course if you use its own Fourier transform a spectrum you basically create the original image and this is the rectangle image that is reconstruct reconstructed using its face but for the spectrum we

**1:28:08** · use the boys image and again you here see that we can clearly see the rectangle although not hundred percent accurate but this further confirms that between the two spectrum and phase angle phase angle contains more information about the image but again if you refer

**1:28:29** · back to their original equations there is no one to one correspondence between the individual pixel in the original image and individual components in the frequency domain so this table

**1:28:47** · summarizes all the grid Fourier transform definition that we had so we had the definition for the discrete Fourier transform we had the definition for the inverse discrete Fourier transform they had the definition for the Fourier transform spectrum phase angle we talked about the polar representation of the Fourier transform we talked about the power spectrum of the Fourier transform we also talked about the average value and we said that the value

**1:29:18** · of the Fourier transform at location zero is proportional to the average of the original signal because this value is basically talking about the zero frequency component of the frequency domain or in other word it talks about the DC component of their original signal we talked about the periodic behavior of them discrete Fourier transform and it's inverse we saw the

**1:29:49** · definition for the circular convolution and here is the definition for the circular called correlation of course and many of the applications we only care about their circular convolution because if you remember we said that

**1:30:12** · convolution is basically the basis for image filtering then we talked a little bit about the pair ability of them to the discrete Fourier transform you saw an example of it when we applied the Fourier transform on to the two-dimensional box function and we said that we can separate they're basically be composed a complex exponential

**1:30:43** · function into two function and then apply the integrals over one variable and then over another variable so the same can be said about 2d discrete Fourier transform and it can be carefully calculated by computing the one dimensional discrete Fourier transform along the rows for example

**1:31:05** · first and then we apply the one dimensional discrete Fourier transform along the columns and the last definition which we didn't talk about what it is pretty interesting and it can be derived directly from the definitions of the discrete Fourier transform is that you can basically use the exact same algorithm that you use to define the

**1:31:32** · original discrete Fourier transform to perform inverse discrete Fourier transform so to do that no you need to do is you need to provide them complex conjugate oh they're discrete Fourier transform to the algorithm and then it gives you a weighted complex conjugate of the original signal this table

**1:32:01** · summarizes there several discrete Fourier transform pairs that we saw so far we didn't talk about the symmetry property of that much if you're interested you can refer to the table for point one in the book discrete Fourier transform is a general operator so that means that if you apply to sum of two functions the result is basically the summing up them each one of these

**1:32:34** · functions Fourier transform we talked about the translation we talked about how translation can be used to Center their frequency transform by multiplying in the original signal by this function we talked about how rotation would affect this discrete Fourier transform we talked about the convolution theorem and how convolution in the signal domain

**1:33:02** · is equivalent to multiplication in the frequency domain and worse vice versa we didn't talk about correlation here again because what we care about more is the convolution we saw how we can calculate the Fourier transform of a unit impulse

**1:33:23** · without how we can do it for a rectangle function but this one is similar to a 2d box function but it is shifted to location and then a and B here are the definitions for the discrete Fourier transform of sine and cosine function we

**1:33:44** · didn't talk about them but it is good to know that both sine and cosine in the signal domain can be represented f2 individually impulse function in the frequency domain and then we can have the property for the differentiation our

**1:34:02** · function and what if the effect in the frequency domain which we didn't talk about here and then lastly the fact that a Gaussian function in the signal domain is equivalent to a Gaussian function in the frequency domain and vice versa of course there the value for mean and variance of the Gaussian function is going to change so now that we have

### Basics of Filtering in the Frequency Domain

**1:34:29** · covered a lot of theory regarding the Fourier transform and discrete Fourier transform in both one dimensional and two dimensional function it's not the time to talk about basics of filtering in the frequency domain so this is something that I briefly go over and I will talk in more detail in the next

**1:34:54** · lecture so we saw that the Fourier transform is computed by combining all the values of the signal in the spatial domain modified by the values of the exponential term so because of this and as you saw in the example it is impossible to make direct correspondence between a specific components of an image and it's Fourier transform so we

**1:35:20** · cannot have a direct one-to-one correspondence correspondence between one pixel in the image and a frequency component in the Fourier transform domain since the frequency is directly

**1:35:35** · related to the spatial the rate is of change we can associate frequency when the frequency trance with patterns of intensity variations in the image so not necessarily the intensity is itself but how the intensity changes going from one location to another so based on this filtering in the Fourier domain is the

**1:36:02** · act of modifying the Fourier transform to achieve a specific objective followed by inverse Fourier transform to obtain the spatial domain representation of the processed result but this can be formulated like this so we have this a

**1:36:20** · kernel function we have this you can take any function in the frequency domain for which we calculate the elementwise multiplication with the Fourier transform of the original image then what we do is that we calculate the inverse discrete Fourier transform of this multiplication and since the images that we work with or generally only

**1:36:45** · contain real values we calculate the real part of this inverse discrete Fourier transform to get to the process image so based on this we can have a seven step approach for filtering an image in the frequency domain so for the

**1:37:05** · first step we have the input image we call it f of X and y with the size M by n M is the number of roles and n if their number of colored so the first thing that we do is that be zero mirror or replicate pad the original image to form FP R of X of Y with the size P and

**1:37:30** · Q for P being to M and Q being to N and that is to avoid any sort of overlap that we might have in the frequency domain then we multiply this image by this function and the reason for that is

**1:37:50** · we want to Center their Fourier transform so that way the act of defining any transfer function in the frequency domain is much much simpler after the FIR after the second step we calculate the discrete Fourier transform of this multiplication this multiplication function and we get f of U and B which is that Fourier transform

**1:38:22** · of the result of the previous step now to apply any filter we construct a real symmetric filter transfer function H of U and V of size P multiplied by Q so and you can see the size of the filter is the same as the size of their original image and we placed the center of the filter and location P over 2 and Q over 2 so now what we need to do is that we

**1:38:54** · need to form this product G of U and B equals H of U and V multiplied by F of U and B and we do it element wise by element wise multiplication so now after

**1:39:09** · this step we have the Fourier transform of the filtered image so to get their original filter image we need to do several things first we need to calculate the inverse discrete Fourier transform so the inverse discrete Fourier transform is a complex function in general so now since we work with

**1:39:32** · images that are real we take the real part of the result and then to basically reverse the effect of the multiplication that we had at the beginning here we multiply this result by negative 1 to the power x + y x + y at any given location in damage and then finally the final filtered result G of X and y the same side of the input image can be extracted from the M by n region from

**1:40:07** · the top-left quadrant of GP of x and y of course this seven step procedure is all word so it is better if you see in a practical example so here

**1:40:23** · we have an m-by-n scanning electron microscope image but we said the first step is to pad the image to create an image of size 2 M by 2 n so the way we

**1:40:39** · do it is by applying by padding the image with zeros to its right and bottom of course you can apply the zeros uniformly all around the image but this is the easiest way to do and it's much more straightforward then the next step is to multiply this result by the function negative 1 to the power X plus y at any location so this is the result

**1:41:09** · of that multiplication now we apply the 2d discrete Fourier transform and we create both the Fourier transform spectrum and Fourier transform phase angle so this is a representation of the

**1:41:29** · Fourier transform spectrum now let's say here we want to apply a Gaussian low-pass filter to the image so the way we do it we define our Gaussian low-pass filter centered at location P over 2 and n over 2 so basically right at the center and then what we do is we

**1:41:57** · calculate the element wise multiplication between this filter and the Fourier transform not necessarily not only the spectrum but both the spectrum and the phase angle so this is a representation of the spectrum of the product of H and F again we don't only

**1:42:21** · rely on there a spectrum this is only for representation purposes and then the next step would be to calculate the real part of the inverse discrete Fourier transform and multiply it by negative 1 to the power X plus y at any given location so now to get to the final result we basically extract the top left

**1:42:53** · quarter half there of the image and that is the result of applying a Gaussian to third in the frequency domain you might say ok so this is too much work for a simple Gaussian filter but you need to realize that as we discussed before doing this especially when you have

**1:43:17** · larger images and you have large kernel is usually computationally efficient in comparison to performing 2d convolution in the signal domain here you can see more examples of filter in the frequency

**1:43:39** · domain so here we have the original image and here we have the low-pass Gaussian filter similar to the one that we found in the previous lecture but what if you want to apply a high-pass filter by calculating the inverse of this function or if you remember the way that I described last time that not

**1:44:05** · necessarily last time the previous chapter that we can create a high-pass filter only by using a low-pass filter so if we do that and we apply it to the image we basically get an image of this form as you can see all the uniform regions or almost completely suppressed

**1:44:26** · only thing that is left if all the shape information and boundaries of the original image this one is at the result of high-pass filtering but with a little bit of bias on zero frequency terms so this way we

**1:44:50** · don't suppress their uniform region but we enhance their high frequency component and edges of course you will see more examples in the next lecture so

**1:45:06** · in general there are two ways to design filter so you can either specify the filter in the spatial domain or you can specify the filter in the frequency domain because of this there are two ways for implementing any filtering tool you can either use a special convolution or you can use this creat Fourier transform and inverse discrete Fourier transform to apply your filters so here

**1:45:31** · you can see an example of a 1 dimensional Gaussian low-pass filter and this one is the corresponding kernel in the spatial domain of 4d two functions or continuous in reality what you need to do is that you need to sample them and here you see an example of a

**1:45:54** · Gaussian high-pass filter in the frequency domain and you see is corresponding corresponding kernels in their signal domain as well so again these two are continuous in reality you use a sample version of them and here is

**1:46:13** · another example that shows how spatial filtering and frequency filtering if done properly they are producing identical result so here is the original image that we have and here it's full-year spectrum on top left corner here we have a special kernel and a

**1:46:36** · perspective view of its corresponding frequency domain filter transfer function here is the same filter transfer function shown as in an image with the anywhere that you have a dark region you're basically dealing with negative values and energy anywhere you have a bright region here you are dealing with positive values and in in this image on

**1:47:03** · the Left lower left is the result of filtering the original image in the frequency domain with their transfer function defined like this and here is the result of filtering the same image in the spatial domain with the kernel defined like this and as you can see the result are completely identical so this

**1:47:30** · pretty much concludes all the thing that I wanted to talk to you about in this lecture the next lecture I will talk about images smoothing using low pass frequency domain filter image sharpening using high pass frequency domain filters then I talked a little bit about selective filtering and finally I will talk about the fast Fourier transform and why is being used widely in all

**1:47:58** · sorts of different signal and image processing applications

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[Clippings Index#Digital Image Processing|Clippings Index - Digital Image Processing]] · [[Second Brain]] · **Map:** [[MOC]]
> **Prev:** [[05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 5 - Introduction to Fourier Transform|Digital Image Processing - Part 5 - Introduction to Fourier Transform]] · **Next:** [[05 - Second Brain & Knowledge/Clippings/Digital Image Processing/Digital Image Processing - Part 7 - Image Filtering in Frequency Domain|Digital Image Processing - Part 7 - Image Filtering in Frequency Domain]]
> **Related:** [[IPA]] · [[Probability & Statistics]] · [[AI & ML Roadmap]]
<!-- connections:end -->
