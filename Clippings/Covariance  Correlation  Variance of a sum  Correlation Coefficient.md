---
title: "Covariance | Correlation | Variance of a sum | Correlation Coefficient:"
source: "https://www.probabilitycourse.com/chapter5/5_3_1_covariance_correlation.php"
author:
published:
created: 2025-11-11
description:
tags:
  - "clippings"
---
---

  

## 5.3.1 Covariance and Correlation

Consider two random variables $X$ and $Y$ . Here, we define the **covariance** between $X$ and $Y$ , written $Cov(X,Y)$ . The covariance gives some information about how $X$ and $Y$ are statistically related. Let us provide the definition, then discuss the properties and applications of covariance.

The **covariance** between $X$ and $Y$ is defined as 
$$
Cov(X,Y)=E[(X−EX)(Y−EY)]=E[XY]−(EX)(EY).
$$

Note that 
$$
E[(X−EX)(Y−EY)]=E[XY−X(EY)−(EX)Y+(EX)(EY)]=E[XY]−(EX)(EY)−(EX)(EY)+(EX)(EY)=E[XY]−(EX)(EY).
$$
Intuitively, the covariance between $X$ and $Y$ indicates how the values of $X$ and $Y$ move relative to each other. If large values of $X$ tend to happen with large values of $Y$ , then $(X−EX)(Y−EY)$ is positive on average. In this case, the covariance is positive and we say $X$ and $Y$ are positively correlated. On the other hand, if $X$ tends to be small when $Y$ is large, then $(X−EX)(Y−EY)$ is negative on average. In this case, the covariance is negative and we say $X$ and $Y$ are negatively correlated.  

---

Example  
Suppose $X∼Uniform(1,2)$ , and given $X=x$ , $Y$ is exponential with parameter $λ=x$ . Find $Cov(X,Y)$ .

- **Solution**
	- We can use Cov $(X,Y)=EXY−EXEY$ . We have $EX=32$ and 
		$$
		EY=E[E[Y|X]](law of iterated expectations (Equation 5.17))=E[1X](since Y|X∼Exponential(X))=∫121xdx=ln⁡2.
		$$
		We also have 
		$$
		EXY=E[E[XY|X]](law of iterated expectations)EXY=E[XE[Y|X]](sinceE[X|X=x]=x)=E[X1X](since Y|X∼Exponential(X))=1.
		$$
		Thus,
		$$
		Cov(X,Y)=E[XY]−(EX)(EY)=1−32ln⁡2.
		$$

---

  
Now we discuss the properties of covariance.

Lemma  
The covariance has the following properties:
1. $Cov(X,X)=Var(X)$ ;
2. if $X$ and $Y$ are independent then $Cov(X,Y)=0$ ;
3. $Cov(X,Y)=Cov(Y,X)$ ;
4. $Cov(aX,Y)=aCov(X,Y)$ ;
5. $Cov(X+c,Y)=Cov(X,Y)$ ;
6. $Cov(X+Y,Z)=Cov(X,Z)+Cov(Y,Z)$ ;
7. more generally,
$$
Cov(∑i=1maiXi,∑j=1nbjYj)=∑i=1m∑j=1naibjCov(Xi,Yj).
$$

All of the above results can be proven directly from the definition of covariance. For example, if $X$ and $Y$ are independent, then as we have seen before $E[XY]=EXEY$ , so 
$$
Cov(X,Y)=E[XY]−EXEY=0.
$$
Note that the converse is not necessarily true. That is, if $Cov(X,Y)=0$ , $X$ and $Y$ may or may not be independent. Let us prove Item 6 in Lemma 5.3, $Cov(X+Y,Z)=Cov(X,Z)+Cov(Y,Z)$ . We have 
$$
Cov(X+Y,Z)=E[(X+Y)Z]−E(X+Y)EZ=E[XZ+YZ]−(EX+EY)EZ=EXZ−EXEZ+EYZ−EYEZ=Cov(X,Z)+Cov(Y,Z).
$$
You can prove the rest of the items in Lemma 5.3 similarly.

---

Example  
Let $X$ and $Y$ be two independent $N(0,1)$ random variables and 
$$
Z=1+X+XY2,W=1+X.
$$
Find Cov $(Z,W)$ .

- **Solution**
	- $$
		Cov(Z,W)=Cov(1+X+XY2,1+X)=Cov(X+XY2,X)(by part 5 of Lemma 5.3)=Cov(X,X)+Cov(XY2,X)(by part 6 of Lemma 5.3)=Var(X)+E[X2Y2]−E[XY2]EX(by part 1 of Lemma 5.3 & definition of Cov)=1+E[X2]E[Y2]−E[X]2E[Y2](since X and Y are independent)=1+1−0=2.
		$$

---

  

## Variance of a sum:

One of the applications of covariance is finding the variance of a sum of several random variables. In particular, if $Z=X+Y$ , then 
$$
Var(Z)=Cov(Z,Z)=Cov(X+Y,X+Y)=Cov(X,X)+Cov(X,Y)+Cov(Y,X)+Cov(Y,Y)=Var(X)+Var(Y)+2Cov(X,Y).
$$
More generally, for $a,b∈R$ , we conclude:
$$
Var(aX+bY)=a2Var(X)+b2Var(Y)+2abCov(X,Y)(5.21)
$$
  

## Correlation Coefficient:

The **correlation coefficient**, denoted by $ρXY$ or $ρ(X,Y)$ , is obtained by normalizing the covariance. In particular, we define the correlation coefficient of two random variables $X$ and $Y$ as the covariance of the standardized versions of $X$ and $Y$ . Define the standardized versions of $X$ and $Y$ as 
$$
U=X−EXσX,V=Y−EYσY(5.22)
$$
 Then,
$$
ρXY=Cov(U,V)=Cov(X−EXσX,Y−EYσY)=Cov(XσX,YσY)(by Item 5 of Lemma 5.3)=Cov(X,Y)σXσY.
$$
$$
ρXY=ρ(X,Y)=Cov(X,Y)Var(X) Var(Y)=Cov(X,Y)σXσY
$$
  
A nice thing about the correlation coefficient is that it is always between $−1$ and $1$ . This is an immediate result of Cauchy-Schwarz inequality that is discussed in Section 6.2.4. One way to prove that $−1≤ρ≤1$ is to use the following inequality: 
$$
αβ≤α2+β22,for α,β∈R.
$$
This is because $(α−β)2≥0$ . The equality holds only if $α=β$ . From this, we can conclude that for any two random variables $U$ and $V$ , 
$$
E[UV]≤EU2+EV22,
$$
with equality only if $U=V$ with probability one. Now, let $U$ and $V$ be the standardized versions of $X$ and $Y$ as defined in Equation 5.22. Then, by definition $ρXY=Cov(U,V)=EUV$ . But since $EU2=EV2=1$ , we conclude 
$$
ρXY=E[UV]≤EU2+EV22=1,
$$
with equality only if $U=V$ . That is,
$$
Y−EYσY=X−EXσX,
$$
which implies 
$$
Y=σYσXX+(EY−σYσXEX)=aX+b,where a and b are constants.
$$
Replacing $X$ by $−X$ , we conclude that 
$$
ρ(−X,Y)≤1.
$$
But $ρ(−X,Y)=−ρ(X,Y)$ , thus we conclude $ρ(X,Y)≥−1$ . Thus, we can summarize some properties of the correlation coefficient as follows.

Properties of the correlation coefficient:
1. $−1≤ρ(X,Y)≤1$ ;
2. if $ρ(X,Y)=1$ , then $Y=aX+b$ , where $a>0$ ;
3. if $ρ(X,Y)=−1$ , then $Y=aX+b$ , where $a<0$ ;
4. $ρ(aX+b,cY+d)=ρ(X,Y)$ for $a,c>0$ .

  
Definition  
Consider two random variables $X$ and $Y$ :  
\- If $ρ(X,Y)=0$ , we say that $X$ and $Y$ are **uncorrelated**.  
\- If $ρ(X,Y)>0$ , we say that $X$ and $Y$ are **positively** correlated.  
\- If $ρ(X,Y)<0$ , we say that $X$ and $Y$ are **negatively** correlated.  

---

  
Note that as we discussed previously, two independent random variables are always uncorrelated, but the converse is not necessarily true. That is, if $X$ and $Y$ are uncorrelated, then $X$ and $Y$ may or may not be independent. Also, note that if $X$ and $Y$ are uncorrelated from Equation 5.21, we conclude that $Var(X+Y)=Var(X)+Var(Y)$ .  
Note that if $X$ and $Y$ are independent, then they are uncorrelated, and so $Var(X+Y)=Var(X)+Var(Y)$ . This is a fact that we stated previously in [Chapter 3](https://www.probabilitycourse.com/chapter5/chapter3/3_1_1_random_variables.php), and now we could easily prove using covariance.

---

Example  
Let $X$ and $Y$ be as in Example 5.24 in Section 5.2.3, i.e., suppose that we choose a point $(X,Y)$ uniformly at random in the unit disc 
$$
D={(x,y)|x2+y2≤1}.
$$
Are $X$ and $Y$ uncorrelated?

- **Solution**
	- We need to check whether $Cov(X,Y)=0$ . First note that, in [Example 5.24](https://www.probabilitycourse.com/chapter5/chapter5/5_2_3_conditioning_independence.php#example5_24) of [Section 5.2.3](https://www.probabilitycourse.com/chapter5/chapter5/5_2_3_conditioning_independence.php), we found out that $X$ and $Y$ are not independent and in fact, we found that 
		$$
		X|Y∼Uniform(−1−Y2,1−Y2).
		$$
		Now let's find $Cov(X,Y)=EXY−EXEY$ . We have 
		$$
		EX=E[E[X|Y]](law of iterated expectations (Equation 5.17))=E[0]=0(since X|Y∼Uniform(−1−Y2,1−Y2)).
		$$
		Also, we have 
		$$
		E[XY]=E[E[XY|Y]](law of iterated expectations (Equation 5.17))=E[YE[X|Y]](Equation 5.6)=E[Y⋅0]=0.
		$$
		Thus,
		$$
		Cov(X,Y)=E[XY]−EXEY=0.
		$$
		Thus, $X$ and $Y$ are uncorrelated.

---