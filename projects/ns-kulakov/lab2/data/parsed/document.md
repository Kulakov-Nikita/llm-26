# OpenIntro Statistics, 4th edition

## 5.1 — Point estimates and sampling variability

### PDF page 168

168

Chapter 5

Foundations for inference





5.1 Point estimates and sampling variability

5.2 Conﬁdence intervals for a proportion

5.3 Hypothesis testing for a proportion

---

# OpenIntro Statistics, 4th edition

## 5.1 — Point estimates and sampling variability

### PDF page 169

169





Statistical inference  is primarily concerned with understanding and

quantifying the uncertainty of parameter estimates. While the equa-

tions and details change depending on the setting, the foundations for

inference are the same throughout all of statistics.


We start with a familiar topic: the idea of using a sample proportion

to estimate a population proportion. Next, we create what’s called a

conﬁdence interval, which is a range of plausible values where we may

ﬁnd the true population value.  Finally, we introduce the hypothesis

testing framework, which allows us to formally evaluate claims about

the population, such as whether a survey provides strong evidence that

a candidate has the support of a majority of the voting population.





For videos, slides, and other resources, please visit
www.openintro.org/os

---

# OpenIntro Statistics, 4th edition

## 5.1 — Point estimates and sampling variability

### PDF page 170

170                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE


        5.1  Point estimates and sampling variability



                Companies such as Pew Research frequently conduct polls as a way to understand the state
                of public opinion or knowledge on many topics, including politics, scientiﬁc understanding, brand
               recognition, and more. The ultimate goal in taking a poll is generally to use the responses to estimate
              the opinion or knowledge of the broader population.


            5.1.1  Point estimates and error

                 Suppose a poll suggested the US President’s approval rating is 45%. We would consider 45% to
             be a point estimate of the approval rating we might see if we collected responses from the entire
              population. This entire-population response proportion is generally referred to as the parameter
                of interest. When the parameter is a proportion, it is often denoted by p, and we often refer to the
             sample proportion as ˆp (pronounced p-hat1). Unless we collect responses from every individual in
              the population, p remains unknown, and we use ˆp as our estimate of p. The diﬀerence we observe
             from the poll versus the parameter is called the error in the estimate. Generally, the error consists
                of two aspects: sampling error and bias.
               Sampling error, sometimes called sampling uncertainty, describes how much an estimate will
             tend to vary from one sample to the next. For instance, the estimate from one sample might be 1%
              too low while in another it may be 3% too high. Much of statistics, including much of this book,
                   is focused on understanding and quantifying sampling error, and we will ﬁnd it useful to consider a
              sample’s size to help us quantify this error; the sample size is often represented by the letter n.
                Bias describes a systematic tendency to over- or under-estimate the true population value.
             For example, if we were taking a student poll asking about support for a new college stadium, we’d
             probably get a biased estimate of the stadium’s level of student support by wording the question as,
          Do you support your school by supporting funding for the new stadium? We try to minimize bias
             through thoughtful data collection procedures, which were discussed in Chapter 1 and are the topic
                of many other books.


            5.1.2  Understanding the variability of a point estimate

                 Suppose the proportion of American adults who support the expansion of solar energy is p =
                0.88, which is our parameter of interest.2 If we were to take a poll of 1000 American adults on this
                topic, the estimate would not be perfect, but how close might we expect the sample proportion in
              the poll would be to 88%? We want to understand, how does the sample proportion ˆp behave when
               the true population proportion is 0.88.3  Let’s ﬁnd out! We can simulate responses we would get
             from a simple random sample of 1000 American adults, which is only possible because we know the
               actual support for expanding solar energy is 0.88. Here’s how we might go about constructing such
             a simulation:

                    1. There were about 250 million American adults in 2018. On 250 million pieces of paper, write
                   “support” on 88% of them and “not” on the other 12%.

                    2. Mix up the pieces of paper and pull out 1000 pieces to represent our sample of 1000 American
                     adults.

                    3. Compute the fraction of the sample that say “support”.

           Any volunteers to conduct this simulation? Probably not. Running this simulation with 250 million
               pieces of paper would be time-consuming and very costly, but we can simulate it using computer

                 1Not to be confused with phat, the slang term used for something cool, like this book.
               2We haven’t actually conducted a census to measure this value perfectly.  However, a very large sample has
                suggested the actual level of support is about 88%.
                388% written as a proportion would be 0.88. It is common to switch between proportion and percent. However,
                formulas presented in this book always refer to the proportion, not the percent.

---

# OpenIntro Statistics, 4th edition

## 5.1 — Point estimates and sampling variability

### PDF page 171

5.1. POINT ESTIMATES AND SAMPLING VARIABILITY                                          171


code; we’ve written a short program in Figure 5.1 in case you are curious what the computer code
looks like.  In this simulation, the sample gave a point estimate of  ˆp1 = 0.894. We know the
population proportion for the simulation was p = 0.88, so we know the estimate had an error of
0.894 −0.88 = +0.014.

# 1. Create a set of 250 million entries, where 88% of them are "support"
#    and 12% are "not".
pop size <- 250000000
possible entries <- c(rep("support", 0.88 * pop size), rep("not", 0.12 * pop size))

# 2. Sample 1000 entries without replacement.
sampled entries <- sample(possible entries, size = 1000)

# 3. Compute p-hat: count the number that are "support", then divide by
#    the sample size.
sum(sampled entries == "support") / 1000

        Figure 5.1: For those curious, this is code for a single ˆp simulation using the statis-
          tical software called R. Each line that starts with # is a code comment, which is
        used to describe in regular language what the code is doing. We’ve provided soft-
       ware labs in R at openintro.org/stat/labs for anyone interested in learning more.


    One simulation isn’t enough to get a great sense of the distribution of estimates we might expect
in the simulation, so we should run more simulations. In a second simulation, we get ˆp2 = 0.885,
which has an error of +0.005. In another, ˆp3 = 0.878 for an error of -0.002. And in another, an
estimate of ˆp4 = 0.859 with an error of -0.021. With the help of a computer, we’ve run the simulation
10,000 times and created a histogram of the results from all 10,000 simulations in Figure 5.2. This
distribution of sample proportions is called a sampling distribution. We can characterize this
sampling distribution as follows:

Center. The center of the distribution is ¯xˆp = 0.880, which is the same as the parameter. Notice
     that the simulation mimicked a simple random sample of the population, which is a straight-
     forward sampling strategy that helps avoid sampling bias.

Spread. The standard deviation of the distribution is sˆp = 0.010. When we’re talking about a
     sampling distribution or the variability of a point estimate, we typically use the term standard
     error rather than standard deviation, and the notation SEˆp is used for the standard error
      associated with the sample proportion.

Shape. The distribution is symmetric and bell-shaped, and it resembles a normal distribution.

These ﬁndings are encouraging! When the population proportion is p = 0.88 and the sample size is
n = 1000, the sample proportion ˆp tends to give a pretty good estimate of the population proportion.
We also have the interesting observation that the histogram resembles a normal distribution.


  SAMPLING DISTRIBUTIONS ARE NEVER OBSERVED, BUT WE KEEP THEM IN MIND
  In real-world applications, we never actually observe the sampling distribution, yet it is useful to
  always think of a point estimate as coming from such a hypothetical distribution. Understanding
  the sampling distribution will help us characterize and make sense of the point estimates that
  we do observe.



EXAMPLE 5.1
If we used a much smaller sample size of n = 50, would you guess that the standard error for ˆp
would be larger or smaller than when we used n = 1000?

Intuitively, it seems like more data is better than less data, and generally that is correct! The typical
error when p = 0.88 and n = 50 would be larger than the error we would expect when n = 1000.


    Example 5.1 highlights an important property we will see again and again: a bigger sample
tends to provide a more precise point estimate than a smaller sample.

---

# OpenIntro Statistics, 4th edition

## 5.1 — Point estimates and sampling variability

### PDF page 172

172                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE



                          750

                                                                                Frequency 500                          250


                            0
                                   0.84            0.86            0.88            0.90            0.92
                                                    Sample Proportions

                      Figure 5.2: A histogram of 10,000 sample proportions, where each sample is taken
                    from a population where the population proportion is 0.88 and the sample size is
                 n = 1000.


            5.1.3  Central Limit Theorem

               The distribution in Figure 5.2 looks an awful lot like a normal distribution. That is no anomaly;
                    it is the result of a general principle called the Central Limit Theorem.


            CENTRAL LIMIT THEOREM AND THE SUCCESS-FAILURE CONDITION
            When observations are independent and the sample size is suﬃciently large, the sample propor-
                 tion ˆp will tend to follow a normal distribution with the following mean and standard error:

                                  r p(1 −p)
                                                 µˆp = p                      SEˆp =
                                                             n

                In order for the Central Limit Theorem to hold, the sample size is typically considered suﬃciently
                  large when np ≥10 and n(1 −p) ≥10, which is called the success-failure condition.


               The Central Limit Theorem is incredibly important, and it provides a foundation for much
                of statistics. As we begin applying the Central Limit Theorem, be mindful of the two technical
               conditions: the observations must be independent, and the sample size must be suﬃciently large
              such that np ≥10 and n(1 −p) ≥10.


          EXAMPLE 5.2
               Earlier we estimated the mean and standard error of ˆp using simulated data when p = 0.88 and
           n = 1000. Conﬁrm that the Central Limit Theorem applies and the sampling distribution is ap-
              proximately normal.


            Independence. There are n = 1000 observations for each sample proportion ˆp, and each of those
                    observations are independent draws. The most common way for observations to be considered
                   independent is if they are from a simple random sample.

             Success-failure condition. We can conﬁrm the sample size is suﬃciently large by checking the
                      success-failure condition and conﬁrming the two calculated values are greater than 10:

                       np = 1000 × 0.88 = 880 ≥10       n(1 −p) = 1000 × (1 −0.88) = 120 ≥10


           The independence and success-failure conditions are both satisﬁed, so the Central Limit Theorem
                applies, and it’s reasonable to model ˆp using a normal distribution.

---

# OpenIntro Statistics, 4th edition

## 5.1 — Point estimates and sampling variability

### PDF page 173

5.1. POINT ESTIMATES AND SAMPLING VARIABILITY                                          173



 HOW TO VERIFY SAMPLE OBSERVATIONS ARE INDEPENDENT
  Subjects in an experiment are considered independent if they undergo random assignment to
  the treatment groups.

   If the observations are from a simple random sample, then they are independent.

   If a sample is from a seemingly random process, e.g. an occasional error on an assembly line,
  checking independence is more diﬃcult. In this case, use your best judgement.


   An additional condition that is sometimes added for samples from a population is that they
are no larger than 10% of the population. When the sample exceeds 10% of the population size, the
methods we discuss tend to overestimate the sampling error slightly versus what we would get using
more advanced methods.4 This is very rarely an issue, and when it is an issue, our methods tend to
be conservative, so we consider this additional check as optional.


EXAMPLE 5.3
Compute the theoretical mean and standard error of ˆp when p = 0.88 and n = 1000, according to
the Central Limit Theorem.

The mean of the ˆp’s is simply the population proportion: µˆp = 0.88.

The calculation of the standard error of ˆp uses the following formula:

               r p(1 −p) r 0.88(1 −0.88)
                         SEˆp =       =          = 0.010
                             n            1000




EXAMPLE 5.4
Estimate how frequently the sample proportion  ˆp should be within 0.02 (2%) of the population
value, p = 0.88. Based on Examples 5.2 and 5.3, we know that the distribution is approximately
N(µˆp = 0.88, SEˆp = 0.010).

After so much practice in Section 4.1, this normal distribution example will hopefully feel familiar!
We would like to understand the fraction of ˆp’s between 0.86 and 0.90:





                                   0.86    0.88    0.90

With µˆp = 0.88 and SEˆp = 0.010, we can compute the Z-score for both the left and right cutoﬀs:

                         0.86 −0.88                               0.90 −0.88
                 Z0.86 =       = −2                 Z0.90 =       = 2
                           0.010                                   0.010

We can use either statistical software, a graphing calculator, or a table to ﬁnd the areas to the tails,
and in any case we will ﬁnd that they are each 0.0228. The total tail areas are 2 × 0.0228 = 0.0456,
which leaves the shaded area of 0.9544.  That is, about 95.44% of the sampling distribution in
Figure 5.2 is within ±0.02 of the population proportion, p = 0.88.





   4For example, we could use what’s called the ﬁnite population correction factor:  if the sample is of size n
                                       q N−n
and the population size is N, then we can multiple the typical standard error formula by  N−1 to obtain a smaller,
more precise estimate of the actual standard error. When n < 0.1 × N, this correction factor is relatively small.

---

# OpenIntro Statistics, 4th edition

## 5.1 — Point estimates and sampling variability

### PDF page 174

174                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE



           GUIDED PRACTICE 5.5
              In Example 5.1 we discussed how a smaller sample would tend to produce a less reliable estimate.
                                   q p(1−p)
             Explain how this intuition is reﬂected in the formula for SEˆp =     n   .5




            5.1.4  Applying the Central Limit Theorem to a real-world setting

            We do not actually know the population proportion unless we conduct an expensive poll of all
               individuals in the population. Our earlier value of p = 0.88 was based on a Pew Research conducted
             a poll of 1000 American adults that found ˆp = 0.887 of them favored expanding solar energy. The
               researchers might have wondered: does the sample proportion from the poll approximately follow a
             normal distribution? We can check the conditions from the Central Limit Theorem:

            Independence. The poll is a simple random sample of American adults, which means that the
                    observations are independent.

             Success-failure condition. To check this condition, we need the population proportion, p, to
                   check if both np and n(1 −p) are greater than 10. However, we do not actually know p, which
                           is exactly why the pollsters would take a sample! In cases like these, we often use ˆp as our
                   next best way to check the success-failure condition:

                                   nˆp = 1000 × 0.887 = 887          n(1 −ˆp) = 1000 × (1 −0.887) = 113

                The sample proportion ˆp acts as a reasonable substitute for p during this check, and each value
                      in this case is well above the minimum of 10.

                  This substitution approximation of using ˆp in place of p is also useful when computing the
              standard error of the sample proportion:

                  r p(1 −p) r ˆp(1 −ˆp) r 0.887(1 −0.887)
                               SEˆp =       ≈       =           = 0.010
                                  n         n             1000

             This substitution technique is sometimes referred to as the “plug-in principle”. In this case, SEˆp
               didn’t change enough to be detected using only 3 decimal places versus when we completed the
               calculation with 0.88 earlier. The computed standard error tends to be reasonably stable even when
              observing slightly diﬀerent proportions in one sample or another.





                    5Since the sample size n is in the denominator (on the bottom) of the fraction, a bigger sample size means the
                   entire expression when calculated will tend to be smaller. That is, a larger sample size would correspond to a smaller
                standard error.

---

# OpenIntro Statistics, 4th edition

## 5.1 — Point estimates and sampling variability

### PDF page 175

5.1. POINT ESTIMATES AND SAMPLING VARIABILITY                                          175


5.1.5  More details regarding the Central Limit Theorem

We’ve applied the Central Limit Theorem in numerous examples so far this chapter:

    When observations are independent and the sample size is suﬃciently large, the distri-
      bution of ˆp resembles a normal distribution with

                           r p(1 −p)
                                 µˆp = p                    SEˆp =
                                                 n

    The sample size is considered suﬃciently large when np ≥10 and n(1 −p) ≥10.

In this section, we’ll explore the success-failure condition and seek to better understand the Central
Limit Theorem.
   An interesting question to answer is, what happens when np < 10 or n(1 −p) < 10? As we did
in Section 5.1.2, we can simulate drawing samples of diﬀerent sizes where, say, the true proportion
is p = 0.25. Here’s a sample of size 10:

                              no, no, yes, yes, no, no, no, no, no, no
In this sample, we observe a sample proportion of yeses of ˆp = 102 = 0.2. We can simulate many such
proportions to understand the sampling distribution of ˆp when n = 10 and p = 0.25, which we’ve
plotted in Figure 5.3 alongside a normal distribution with the same mean and variability. These
distributions have a number of important diﬀerences.



     2000

     1000      Frequency

        0
             0.0  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8          −0.2      0.0       0.2       0.4       0.6
                      Sample Proportions

        Figure 5.3: Left: simulations of ˆp when the sample size is n = 10 and the population
        proportion is p = 0.25. Right: a normal distribution with the same mean (0.25)
       and standard deviation (0.137).


                                    Unimodal?  Smooth?  Symmetric?
                Normal: N(0.25, 0.14)     Yes      Yes       Yes
              n = 10, p = 0.25         Yes      No       No

Notice that the success-failure condition was not satisﬁed when n = 10 and p = 0.25:

              np = 10 × 0.25 = 2.5               n(1 −p) = 10 × 0.75 = 7.5

This single sampling distribution does not show that the success-failure condition is the perfect
guideline, but we have found that the guideline did correctly identify that a normal distribution
might not be appropriate.
   We can complete several additional simulations, shown in Figures 5.4 and 5.5, and we can see
some trends:

   1. When either np or n(1 −p) is small, the distribution is more discrete, i.e. not continuous.

   2. When np or n(1 −p) is smaller than 10, the skew in the distribution is more noteworthy.

   3. The larger both np and n(1−p), the more normal the distribution. This may be a little harder
      to see for the larger sample size in these plots as the variability also becomes much smaller.

   4. When np and n(1 −p) are both very large, the distribution’s discreteness is hardly evident,
     and the distribution looks much more like a normal distribution.

---

# OpenIntro Statistics, 4th edition

## 5.1 — Point estimates and sampling variability

### PDF page 176

176                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE


                      n = 10             n = 25



         p = 0.1


                                                    0.0      0.2      0.4      0.6      0.8      1.0        0.0      0.2      0.4      0.6      0.8      1.0


         p = 0.2


                                                    0.0      0.2      0.4      0.6      0.8      1.0        0.0      0.2      0.4      0.6      0.8      1.0


         p = 0.5


                                                    0.0      0.2      0.4      0.6      0.8      1.0        0.0      0.2      0.4      0.6      0.8      1.0


         p = 0.8


                                                    0.0      0.2      0.4      0.6      0.8      1.0        0.0      0.2      0.4      0.6      0.8      1.0


         p = 0.9


                                                    0.0      0.2      0.4      0.6      0.8      1.0        0.0      0.2      0.4      0.6      0.8      1.0



                      Figure 5.4: Sampling distributions for several scenarios of p and n.
                    Rows: p = 0.10, p = 0.20, p = 0.50, p = 0.80, and p = 0.90.
                    Columns: n = 10 and n = 25.

---

# OpenIntro Statistics, 4th edition

## 5.1 — Point estimates and sampling variability

### PDF page 177

5.1. POINT ESTIMATES AND SAMPLING VARIABILITY                                          177


     n = 50          n = 100         n = 250





    0.0    0.2    0.4    0.6    0.8    1.0       0.0    0.2    0.4    0.6    0.8    1.0       0.0    0.2    0.4    0.6    0.8    1.0





    0.0    0.2    0.4    0.6    0.8    1.0       0.0    0.2    0.4    0.6    0.8    1.0       0.0    0.2    0.4    0.6    0.8    1.0





    0.0    0.2    0.4    0.6    0.8    1.0       0.0    0.2    0.4    0.6    0.8    1.0       0.0    0.2    0.4    0.6    0.8    1.0





    0.0    0.2    0.4    0.6    0.8    1.0       0.0    0.2    0.4    0.6    0.8    1.0       0.0    0.2    0.4    0.6    0.8    1.0





    0.0    0.2    0.4    0.6    0.8    1.0       0.0    0.2    0.4    0.6    0.8    1.0       0.0    0.2    0.4    0.6    0.8    1.0



        Figure 5.5: Sampling distributions for several scenarios of p and n.
       Rows: p = 0.10, p = 0.20, p = 0.50, p = 0.80, and p = 0.90.
       Columns: n = 50, n = 100, and n = 250.

---

# OpenIntro Statistics, 4th edition

## 5.1 — Point estimates and sampling variability

### PDF page 178

178                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE


                So far we’ve only focused on the skew and discreteness of the distributions. We haven’t con-
               sidered how the mean and standard error of the distributions change. Take a moment to look back
               at the graphs, and pay attention to three things:

                    1. The centers of the distribution are always at the population proportion, p, that was used to
                    generate the simulation.  Because the sampling distribution of  ˆp is always centered at the
                   population parameter p, it means the sample proportion ˆp is unbiased when the data are
                   independent and drawn from such a population.

                    2. For a particular population proportion p, the variability in the sampling distribution decreases
                    as the sample size n becomes larger. This will likely align with your intuition: an estimate
                  based on a larger sample size will tend to be more accurate.

                    3. For a particular sample size, the variability will be largest when p = 0.5. The diﬀerences may
                  be a little subtle, so take a close look. This reﬂects the role of the proportion p in the standard
                  q p(1−p)
                     error formula: SE =     n    . The standard error is largest when p = 0.5.

                At no point will the distribution of ˆp look perfectly normal, since ˆp will always be take discrete
               values (x/n). It is always a matter of degree, and we will use the standard success-failure condition
             with minimums of 10 for np and n(1 −p) as our guideline within this book.


            5.1.6  Extending the framework for other statistics

               The strategy of using a sample statistic to estimate a parameter is quite common, and it’s
             a strategy that we can apply to other statistics besides a proportion. For instance, if we want to
              estimate the average salary for graduates from a particular college, we could survey a random sample
                of recent graduates; in that example, we’d be using a sample mean ¯x to estimate the population
           mean µ for all graduates. As another example,  if we want to estimate the diﬀerence in product
                prices for two websites, we might take a random sample of products available on both sites, check
              the prices on each, and use then compute the average diﬀerence; this strategy certainly would give
              us some idea of the actual diﬀerence through a point estimate.
                 While this chapter emphases a single proportion context, we’ll encounter many diﬀerent con-
               texts throughout this book where these methods will be applied. The principles and general ideas
               are the same, even if the details change a little. We’ve also sprinkled some other contexts into the
                exercises to help you start thinking about how the ideas generalize.

---

# OpenIntro Statistics, 4th edition

## 5.1 — Point estimates and sampling variability

### PDF page 179

5.1. POINT ESTIMATES AND SAMPLING VARIABILITY                                          179


Exercises


5.1  Identify the parameter, Part I. For each of the following situations, state whether the parameter of
interest is a mean or a proportion. It may be helpful to examine whether individual responses are numerical
or categorical.

(a) In a survey, one hundred college students are asked how many hours per week they spend on the Internet.
(b) In a survey, one hundred college students are asked: “What percentage of the time you spend on the
    Internet is part of your course work?”
(c) In a survey, one hundred college students are asked whether or not they cited information from Wikipedia
    in their papers.
(d) In a survey, one hundred college students are asked what percentage of their total weekly spending is
    on alcoholic beverages.
(e) In a sample of one hundred recent college graduates, it is found that 85 percent expect to get a job
    within one year of their graduation date.

5.2  Identify the parameter, Part II. For each of the following situations, state whether the parameter of
interest is a mean or a proportion.

(a) A poll shows that 64% of Americans personally worry a great deal about federal spending and the budget
    deﬁcit.
(b) A survey reports that local TV news has shown a 17% increase in revenue within a two year period
    while newspaper revenues decreased by 6.4% during this time period.
(c) In a survey, high school and college students are asked whether or not they use geolocation services on
     their smart phones.
(d) In a survey, smart phone users are asked whether or not they use a web-based taxi service.
(e) In a survey, smart phone users are asked how many times they used a web-based taxi service over the
     last year.

5.3  Quality control. As part of a quality control process for computer chips, an engineer at a factory
randomly samples 212 chips during a week of production to test the current rate of chips with severe defects.
She ﬁnds that 27 of the chips are defective.

(a) What population is under consideration in the data set?
(b) What parameter is being estimated?
(c) What is the point estimate for the parameter?
(d) What is the name of the statistic can we use to measure the uncertainty of the point estimate?
(e) Compute the value from part (d) for this context.
(f) The historical rate of defects is 10%. Should the engineer be surprised by the observed rate of defects
    during the current week?
(g) Suppose the true population value was found to be 10%.  If we use this proportion to recompute the
    value in part (e) using p = 0.1 instead of ˆp, does the resulting value change much?

5.4  Unexpected expense. In a random sample 765 adults in the United States, 322 say they could not
cover a $400 unexpected expense without borrowing money or going into debt.

(a) What population is under consideration in the data set?
(b) What parameter is being estimated?
(c) What is the point estimate for the parameter?
(d) What is the name of the statistic can we use to measure the uncertainty of the point estimate?
(e) Compute the value from part (d) for this context.
(f) A cable news pundit thinks the value is actually 50%. Should she be surprised by the data?
(g) Suppose the true population value was found to be 40%.  If we use this proportion to recompute the
    value in part (e) using p = 0.4 instead of ˆp, does the resulting value change much?

---

# OpenIntro Statistics, 4th edition

## 5.1 — Point estimates and sampling variability

### PDF page 180

180                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE


                5.5  Repeated water samples. A nonproﬁt wants to understand the fraction of households that have
                elevated levels of lead in their drinking water. They expect at least 5% of homes will have elevated levels of
                 lead, but not more than about 30%. They randomly sample 800 homes and work with the owners to retrieve
               water samples, and they compute the fraction of these homes with elevated lead levels. They repeat this
               1,000 times and build a distribution of sample proportions.

                (a) What is this distribution called?
                (b) Would you expect the shape of this distribution to be symmetric, right skewed, or left skewed? Explain
                  your reasoning.
                 (c)  If the proportions are distributed around 8%, what is the variability of the distribution?
                (d) What is the formal name of the value you computed in (c)?
                 (e) Suppose the researchers’ budget is reduced, and they are only able to collect 250 observations per sample,
                  but they can still collect 1,000 samples. They build a new distribution of sample proportions. How will
                   the variability of this new distribution compare to the variability of the distribution when each sample
                   contained 800 observations?

                5.6  Repeated student samples. Of all freshman at a large college, 16% made the dean’s list in the current
                 year. As part of a class project, students randomly sample 40 students and check if those students made
               the list. They repeat this 1,000 times and build a distribution of sample proportions.

                (a) What is this distribution called?
                (b) Would you expect the shape of this distribution to be symmetric, right skewed, or left skewed? Explain
                  your reasoning.
                 (c) Calculate the variability of this distribution.
                (d) What is the formal name of the value you computed in (c)?
                 (e) Suppose the students decide to sample again, this time collecting 90 students per sample, and they again
                      collect 1,000 samples. They build a new distribution of sample proportions. How will the variability
                      of this new distribution compare to the variability of the distribution when each sample contained 40
                    observations?

---

# OpenIntro Statistics, 4th edition

## 5.2 — Confidence intervals for a proportion

### PDF page 181

5.2. CONFIDENCE INTERVALS FOR A PROPORTION                                             181


5.2  Conﬁdence intervals for a proportion



    The sample proportion  ˆp provides a single plausible value for the population proportion p.
However, the sample proportion isn’t perfect and will have some standard error associated with it.
When stating an estimate for the population proportion, it is better practice to provide a plausible
range of values instead of supplying just the point estimate.


5.2.1  Capturing the population parameter

    Using only a point estimate is like ﬁshing in a murky lake with a spear. We can throw a spear
where we saw a ﬁsh, but we will probably miss. On the other hand, if we toss a net in that area,
we have a good chance of catching the ﬁsh. A conﬁdence interval is like ﬁshing with a net, and
it represents a range of plausible values where we are likely to ﬁnd the population parameter.
       If we report a point estimate ˆp, we probably will not hit the exact population proportion. On
the other hand, if we report a range of plausible values, representing a conﬁdence interval, we have
a good shot at capturing the parameter.


GUIDED PRACTICE 5.6
If we want to be very certain we capture the population proportion in an interval, should we use a
wider interval or a smaller interval?6




5.2.2  Constructing a 95% conﬁdence interval

    Our sample proportion ˆp is the most plausible value of the population proportion, so it makes
sense to build a conﬁdence interval around this point estimate. The standard error provides a guide
for how large we should make the conﬁdence interval.
    The standard error represents the standard deviation of the point estimate, and when the Central Limit Theorem conditions are satisﬁed, the point estimate closely follows a normal distribution.
In a normal distribution, 95% of the data is within 1.96 standard deviations of the mean. Using this
principle, we can construct a conﬁdence interval that extends 1.96 standard errors from the sample
proportion to be 95% conﬁdent that the interval captures the population proportion:

                              point estimate ± 1.96 × SE
                         r p(1 −p)
                                                                   ˆp ± 1.96 ×
                                              n

But what does “95% conﬁdent” mean? Suppose we took many samples and built a 95% conﬁdence
interval from each. Then about 95% of those intervals would contain the parameter, p. Figure 5.6
shows the process of creating 25 intervals from 25 samples from the simulation in Section 5.1.2, where
24 of the resulting conﬁdence intervals contain the simulation’s population proportion of p = 0.88,
and one interval does not.





    6If we want to be more certain we will capture the ﬁsh, we might use a wider net.  Likewise, we use a wider
conﬁdence interval if we want to be more certain that we capture the parameter.

---

# OpenIntro Statistics, 4th edition

## 5.2 — Confidence intervals for a proportion

### PDF page 182

182                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE





                                                                     G
                                                                                          G
                                                                             G
                                                                                G
                                                                                      G
                                                                               G
                                                                                           G
                                                                              G
                                                                                                 G
                                                                          G
                                                                                       G
                                                                     G
                                                                                    G
                                                                             G
                                                                                             G
                                                                       G
                                                                             G
                                 GG
                                                                            G
                                                                                 G
                                                                    G
                                                                   G
                                                                              G
                                                                                          G
                                                                                     G

                                                     p = 0.88

                      Figure 5.6: Twenty-ﬁve point estimates and conﬁdence intervals from the sim-
                        ulations in Section 5.1.2.  These intervals are shown relative to the population
                      proportion p = 0.88. Only 1 of these 25 intervals did not capture the population
                       proportion, and this interval has been bolded.



          EXAMPLE 5.7
              In Figure 5.6, one interval does not contain p = 0.88. Does this imply that the population proportion
             used in the simulation could not have been p = 0.88?

              Just as some observations naturally occur more than 1.96 standard deviations from the mean, some
              point estimates will be more than 1.96 standard errors from the parameter of interest. A conﬁdence
                interval only provides a plausible range of values. While we might say other values are implausible
             based on the data, this does not mean they are impossible.



             95% CONFIDENCE INTERVAL FOR A PARAMETER
            When the distribution of a point estimate qualiﬁes for the Central Limit Theorem and therefore
                  closely follows a normal distribution, we can construct a 95% conﬁdence interval as

                                                 point estimate ± 1.96 × SE



          EXAMPLE 5.8
              In Section 5.1 we learned about a Pew Research poll where 88.7% of a random sample of 1000 Amer-
               ican adults supported expanding the role of solar power. Compute and interpret a 95% conﬁdence
                interval for the population proportion.

         We earlier conﬁrmed that ˆp follows a normal distribution and has a standard error of SEˆp = 0.010.
           To compute the 95% conﬁdence interval, plug the point estimate ˆp = 0.887 and standard error into
              the 95% conﬁdence interval formula:

                                              ˆp ± 1.96 × SEˆp →   0.887 ± 1.96 × 0.010 →   (0.8674, 0.9066)

         We are 95% conﬁdent that the actual proportion of American adults who support expanding solar
             power is between 86.7% and 90.7%. (It’s common to round to the nearest percentage point or nearest
              tenth of a percentage point when reporting a conﬁdence interval.)

---

# OpenIntro Statistics, 4th edition

## 5.2 — Confidence intervals for a proportion

### PDF page 183

5.2. CONFIDENCE INTERVALS FOR A PROPORTION                                             183


5.2.3  Changing the conﬁdence level

    Suppose we want to consider conﬁdence intervals where the conﬁdence level is higher than 95%,
such as a conﬁdence level of 99%. Think back to the analogy about trying to catch a ﬁsh: if we want
to be more sure that we will catch the ﬁsh, we should use a wider net. To create a 99% conﬁdence
level, we must also widen our 95% interval. On the other hand, if we want an interval with lower
conﬁdence, such as 90%, we could use a slightly narrower interval than our original 95% interval.
    The 95% conﬁdence interval structure provides guidance in how to make intervals with diﬀerent
conﬁdence levels. The general 95% conﬁdence interval for a point estimate that follows a normal
distribution is

                                point estimate ± 1.96 × SE

There are three components to this interval: the point estimate, “1.96”, and the standard error.
The choice of 1.96 × SE was based on capturing 95% of the data since the estimate is within 1.96
standard errors of the parameter about 95% of the time. The choice of 1.96 corresponds to a 95%
conﬁdence level.


GUIDED PRACTICE 5.9
If X is a normally distributed random variable, what is the probability of the value X being within
2.58 standard deviations of the mean?7

    Guided Practice 5.9 highlights that 99% of the time a normal random variable will be within
2.58 standard deviations of the mean. To create a 99% conﬁdence interval, change 1.96 in the 95%
conﬁdence interval formula to be 2.58. That is, the formula for a 99% conﬁdence interval is

                                  point estimate ± 2.58 × SE



                             99%, extends −2.58 to 2.58


                             95%, extends −1.96 to 1.96





       −3         −2         −1         0          1          2          3
                             Standard Deviations from the Mean

        Figure 5.7: The area between -z⋆and z⋆increases as z⋆becomes larger.  If the
        conﬁdence level is 99%, we choose z⋆such that 99% of a normal normal distribution
           is between -z⋆and z⋆, which corresponds to 0.5% in the lower tail and 0.5% in the
        upper tail: z⋆= 2.58.




   7This is equivalent to asking how often the Z-score will be larger than -2.58 but less than 2.58. For a picture, see
Figure 5.7. To determine this probability, we can use statistical software, a calculator, or a table to look up -2.58
and 2.58 for a normal distribution: 0.0049 and 0.9951. Thus, there is a 0.9951 −0.0049 ≈0.99 probability that an
unobserved normal random variable X will be within 2.58 standard deviations of µ.

---

# OpenIntro Statistics, 4th edition

## 5.2 — Confidence intervals for a proportion

### PDF page 184

184                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE


                  This approach – using the Z-scores in the normal model to compute conﬁdence levels – is
              appropriate when a point estimate such as ˆp is associated with a normal distribution. For some other
              point estimates, a normal model is not a good ﬁt; in these cases, we’ll use alternative distributions
              that better represent the sampling distribution.


             CONFIDENCE INTERVAL USING ANY CONFIDENCE LEVEL
                       If a point estimate closely follows a normal model with standard error SE, then a conﬁdence
                  interval for the population parameter is

                                                 point estimate ± z⋆× SE

               where z⋆corresponds to the conﬁdence level selected.


                  Figure 5.7 provides a picture of how to identify z⋆based on a conﬁdence level. We select z⋆so
              that the area between -z⋆and z⋆in the standard normal distribution, N(0, 1), corresponds to the
             conﬁdence level.


            MARGIN OF ERROR
                In a conﬁdence interval, z⋆× SE is called the margin of error.



          EXAMPLE 5.10
            Use the data in Example 5.8 to create a 90% conﬁdence interval for the proportion of American adults
              that support expanding the use of solar power. We have already veriﬁed conditions for normality.

         We ﬁrst ﬁnd z⋆such that 90% of the distribution falls between -z⋆and z⋆in the standard normal
                distribution, N(µ = 0, σ = 1). We can do this using a graphing calculator, statistical software, or a
               probability table by looking for an upper tail of 5% (the other 5% is in the lower tail): z⋆= 1.65.
           The 90% conﬁdence interval can then be computed as

                                           ˆp ± 1.65 × SEˆp →   0.887 ± 1.65 × 0.0100 →   (0.8705, 0.9035)

            That is, we are 90% conﬁdent that 87.1% to 90.4% of American adults supported the expansion of
                solar power in 2018.



             CONFIDENCE INTERVAL FOR A SINGLE PROPORTION
              Once you’ve determined a one-proportion conﬁdence interval would be helpful for an application,
                 there are four steps to constructing the interval:

              Prepare. Identify ˆp and n, and determine what conﬁdence level you wish to use.

             Check. Verify the conditions to ensure  ˆp is nearly normal.  For one-proportion conﬁdence
                         intervals, use ˆp in place of p to check the success-failure condition.

               Calculate.  If the conditions hold, compute SE using ˆp, ﬁnd z⋆, and construct the interval.

              Conclude. Interpret the conﬁdence interval in the context of the problem.

---

# OpenIntro Statistics, 4th edition

## 5.2 — Confidence intervals for a proportion

### PDF page 185

5.2. CONFIDENCE INTERVALS FOR A PROPORTION                                             185


5.2.4  More case studies

     In New York City on October 23rd, 2014, a doctor who had recently been treating Ebola
patients in Guinea went to the hospital with a slight fever and was subsequently diagnosed with
Ebola. Soon thereafter, an NBC 4 New York/The Wall Street Journal/Marist Poll found that 82%
of New Yorkers favored a “mandatory 21-day quarantine for anyone who has come in contact with an
Ebola patient”. This poll included responses of 1,042 New York adults between Oct 26th and 28th,
2014.


EXAMPLE 5.11
What is the point estimate in this case, and is it reasonable to use a normal distribution to model
that point estimate?

The point estimate, based on a sample of size n = 1042, is  ˆp = 0.82. To check whether  ˆp can
be reasonably modeled using a normal distribution, we check independence (the poll is based on a
simple random sample) and the success-failure condition (1042 × ˆp ≈854 and 1042 × (1 −ˆp) ≈188,
both easily greater than 10). With the conditions met, we are assured that the sampling distribution
of ˆp can be reasonably modeled using a normal distribution.


EXAMPLE 5.12
Estimate the standard error of ˆp = 0.82 from the Ebola survey.

We’ll use the substitution approximation of p ≈ˆp = 0.82 to compute the standard error:

               r p(1 −p) r 0.82(1 −0.82)
                         SEˆp =       ≈          = 0.012
                             n            1042




EXAMPLE 5.13
Construct a 95% conﬁdence interval for p, the proportion of New York adults who supported a
quarantine for anyone who has come into contact with an Ebola patient.

Using the standard error SE = 0.012 from Example 5.12, the point estimate 0.82, and z⋆= 1.96 for
a 95% conﬁdence level, the conﬁdence interval is

         point estimate ± z⋆× SE →   0.82 ± 1.96 × 0.012 →   (0.796, 0.844)

We are 95% conﬁdent that the proportion of New York adults in October 2014 who supported a
quarantine for anyone who had come into contact with an Ebola patient was between 0.796 and
0.844.


GUIDED PRACTICE 5.14
Answer the following two questions about the conﬁdence interval from Example 5.13:8

(a) What does 95% conﬁdent mean in this context?

(b) Do you think the conﬁdence interval is still valid for the opinions of New Yorkers today?





    8(a) If we took many such samples and computed a 95% conﬁdence interval for each, then about 95% of those
intervals would contain the actual proportion of New York adults who supported a quarantine for anyone who has
come into contact with an Ebola patient.
(b) Not necessarily. The poll was taken at a time where there was a huge public safety concern. Now that people have
had some time to step back, they may have changed their opinions. We would need to run a new poll if we wanted
to get an estimate of the current proportion of New York adults who would support such a quarantine period.

---

# OpenIntro Statistics, 4th edition

## 5.2 — Confidence intervals for a proportion

### PDF page 186

186                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE



           GUIDED PRACTICE 5.15
              In the Pew Research poll about solar energy, they also inquired about other forms of energy, and
            84.8% of the 1000 respondents supported expanding the use of wind turbines.9

               (a) Is it reasonable to model the proportion of US adults who support expanding wind turbines
                  using a normal distribution?

              (b) Create a 99% conﬁdence interval for the level of American support for expanding the use of
                wind turbines for power generation.


            We can also construct conﬁdence intervals for other parameters, such as a population mean. In
               these cases, a conﬁdence interval would be computed in a similar way to that of a single proportion:
             a point estimate plus/minus some margin of error. We’ll dive into these details in later chapters.


            5.2.5  Interpreting conﬁdence intervals

                   In each of the examples, we described the conﬁdence intervals by putting them into the context
                of the data and also using somewhat formal language:

              Solar. We are 90% conﬁdent that 87.1% to 90.4% of American adults support the expansion of
                      solar power in 2018.

            Ebola. We are 95% conﬁdent that the proportion of New York adults in October 2014 who sup-
                   ported a quarantine for anyone who had come into contact with an Ebola patient was between
                    0.796 and 0.844.

         Wind Turbine. We are 99% conﬁdent the proportion of Americans adults that support expanding
                   the use of wind turbines is between 81.9% and 87.7% in 2018.

                First, notice that the statements are always about the population parameter, which considers all
            American adults for the energy polls or all New York adults for the quarantine poll.
            We also avoided another common mistake: incorrect language might try to describe the conﬁ-
             dence interval as capturing the population parameter with a certain probability. Making a proba-
                 bility interpretation is a common error: while it might be useful to think of it as a probability, the
             conﬁdence level only quantiﬁes how plausible it is that the parameter is in the given interval.
                 Another important consideration of conﬁdence intervals is that they are only about the popula-
               tion parameter. A conﬁdence interval says nothing about individual observations or point estimates.
            Conﬁdence intervals only provide a plausible range for population parameters.
                     Lastly, keep in mind the methods we discussed only apply to sampling error, not to bias.  If
             a data set is collected in a way that will tend to systematically under-estimate (or over-estimate)
              the population parameter, the techniques we have discussed will not address that problem. Instead,
           we rely on careful data collection procedures to help protect against bias in the examples we have
               considered, which is a common practice employed by data scientists to combat bias.


           GUIDED PRACTICE 5.16
              Consider the 90% conﬁdence interval for the solar energy survey: 87.1% to 90.4%.  If we ran the
              survey again, can we say that we’re 90% conﬁdent that the new survey’s proportion will be between
            87.1% and 90.4%?10


                     9(a) The survey was a random sample and counts are both ≥10 (1000 × 0.848 = 848 and 1000 × 0.152 = 152), so
                independence and the success-failure condition are satisﬁed, and ˆp = 0.848 can be modeled using a normal distribution.
                 (b) Guided Practice 5.15 conﬁrmed that ˆp closely follows a normal distribution, so we can use the C.I. formula:

                                                             point estimate ± z⋆× SE

                 In this case, the point estimate is ˆp = 0.848. For a 99% conﬁdence interval, z⋆= 2.58. Computing the standard error:
           q 0.848(1−0.848)
                SEˆp =        1000   = 0.0114. Finally, we compute the interval as 0.848 ± 2.58 × 0.0114 →(0.8186, 0.8774). It is
                  also important to always provide an interpretation for the interval: we are 99% conﬁdent the proportion of American
                 adults that support expanding the use of wind turbines in 2018 is between 81.9% and 87.7%.
                     10 No, a conﬁdence interval only provides a range of plausible values for a parameter, not future point estimates.

---

# OpenIntro Statistics, 4th edition

## 5.2 — Confidence intervals for a proportion

### PDF page 187

5.2. CONFIDENCE INTERVALS FOR A PROPORTION                                             187


Exercises


5.7  Chronic illness, Part I. In 2013, the Pew Research Foundation reported that “45% of U.S. adults report
that they live with one or more chronic conditions”.11 However, this value was based on a sample, so it may
not be a perfect estimate for the population parameter of interest on its own. The study reported a standard
error of about 1.2%, and a normal model may reasonably be used in this setting. Create a 95% conﬁdence
interval for the proportion of U.S. adults who live with one or more chronic conditions. Also interpret the
conﬁdence interval in the context of the study.

5.8  Twitter users and news, Part I. A poll conducted in 2013 found that 52% of U.S. adult Twitter users get
at least some news on Twitter.12. The standard error for this estimate was 2.4%, and a normal distribution
may be used to model the sample proportion. Construct a 99% conﬁdence interval for the fraction of U.S.
adult Twitter users who get some news on Twitter, and interpret the conﬁdence interval in context.

5.9  Chronic illness, Part II. In 2013, the Pew Research Foundation reported that “45% of U.S. adults
report that they live with one or more chronic conditions”, and the standard error for this estimate is 1.2%.
Identify each of the following statements as true or false. Provide an explanation to justify each of your
answers.

(a) We can say with certainty that the conﬁdence interval from Exercise 5.7 contains the true percentage
     of U.S. adults who suﬀer from a chronic illness.
(b)  If we repeated this study 1,000 times and constructed a 95% conﬁdence interval for each study, then
    approximately 950 of those conﬁdence intervals would contain the true fraction of U.S. adults who suﬀer
    from chronic illnesses.
(c) The poll provides statistically signiﬁcant evidence (at the α = 0.05 level) that the percentage of U.S.
    adults who suﬀer from chronic illnesses is below 50%.
(d) Since the standard error is 1.2%, only 1.2% of people in the study communicated uncertainty about
     their answer.

5.10  Twitter users and news, Part II. A poll conducted in 2013 found that 52% of U.S. adult Twitter users
get at least some news on Twitter, and the standard error for this estimate was 2.4%. Identify each of the
following statements as true or false. Provide an explanation to justify each of your answers.

(a) The data provide statistically signiﬁcant evidence that more than half of U.S. adult Twitter users get
   some news through Twitter.  Use a signiﬁcance level of α = 0.01.  (This part uses concepts from
    Section 5.3 and will be corrected in a future edition.)
(b) Since the standard error is 2.4%, we can conclude that 97.6% of all U.S. adult Twitter users were
    included in the study.
(c)  If we want to reduce the standard error of the estimate, we should collect less data.
(d)  If we construct a 90% conﬁdence interval for the percentage of U.S. adults Twitter users who get
   some news through Twitter, this conﬁdence interval will be wider than a corresponding 99% conﬁdence
     interval.





  11Pew Research Center, Washington, D.C. The Diagnosis Diﬀerence, November 26, 2013.
  12Pew Research Center, Washington, D.C. Twitter News Consumers: Young, Mobile and Educated, November 4,
2013.

---

# OpenIntro Statistics, 4th edition

## 5.2 — Confidence intervals for a proportion

### PDF page 188

188                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE


               5.11  Waiting at an ER, Part I. A hospital administrator hoping to improve wait times decides to estimate
               the average emergency room waiting time at her hospital. She collects a simple random sample of 64 patients
             and determines the time (in minutes) between when they checked in to the ER until they were ﬁrst seen by
              a doctor. A 95% conﬁdence interval based on this sample is (128 minutes, 147 minutes), which is based on
               the normal model for the mean. Determine whether the following statements are true or false, and explain
              your reasoning.

                (a) We are 95% conﬁdent that the average waiting time of these 64 emergency room patients is between
                  128 and 147 minutes.
                (b) We are 95% conﬁdent that the average waiting time of all patients at this hospital’s emergency room is
                  between 128 and 147 minutes.
                 (c) 95% of random samples have a sample mean between 128 and 147 minutes.
                (d) A 99% conﬁdence interval would be narrower than the 95% conﬁdence interval since we need to be more
                    sure of our estimate.
                 (e) The margin of error is 9.5 and the sample mean is 137.5.
                  (f) In order to decrease the margin of error of a 95% conﬁdence interval to half of what it is now, we would
                  need to double the sample size.  (Hint: the margin of error for a mean scales in the same way with
                  sample size as the margin of error for a proportion.)

               5.12  Mental health. The General Social Survey asked the question: “For how many days during the past
              30 days was your mental health, which includes stress, depression, and problems with emotions, not good?”
              Based on responses from 1,151 US residents, the survey reported a 95% conﬁdence interval of 3.40 to 4.24
              days in 2010.

                (a) Interpret this interval in context of the data.
                (b) What does “95% conﬁdent” mean? Explain in the context of the application.
                 (c) Suppose the researchers think a 99% conﬁdence level would be more appropriate for this interval. Will
                      this new interval be smaller or wider than the 95% conﬁdence interval?
                (d)  If a new survey were to be done with 500 Americans, do you think the standard error of the estimate
                 be larger, smaller, or about the same.

               5.13  Website registration. A website is trying to increase registration for ﬁrst-time visitors, exposing 1%
                 of these visitors to a new site design. Of 752 randomly sampled visitors over a month who saw the new
                design, 64 registered.

                (a) Check any conditions required for constructing a conﬁdence interval.
                (b) Compute the standard error.
                 (c) Construct and interpret a 90% conﬁdence interval for the fraction of ﬁrst-time visitors of the site who
                 would register under the new design (assuming stable behaviors by new visitors over time).

               5.14  Coupons driving visits. A store randomly samples 603 shoppers over the course of a year and
              ﬁnds that 142 of them made their visit because of a coupon they’d received in the mail. Construct a 95%
              conﬁdence interval for the fraction of all shoppers during the year whose visit was because of a coupon they’d
                received in the mail.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 189

5.3. HYPOTHESIS TESTING FOR A PROPORTION                                                189


5.3  Hypothesis testing for a proportion



    The following question comes from a book written by Hans Rosling, Anna Rosling R¨onnlund,
and Ola Rosling called Factfulness:

    How many of the world’s 1 year old children today have been vaccinated against some
      disease:

        a. 20%
         b. 50%
         c. 80%

Write down what your answer (or guess), and when you’re ready, ﬁnd the answer in the footnote.13
     In this section, we’ll be exploring how people with a 4-year college degree perform on this and
other world health questions as we learn about hypothesis tests, which are a framework used to
rigorously evaluate competing ideas and claims.


5.3.1  Hypothesis testing framework

    We’re interested in understanding how much people know about world health and development.
If we take a multiple choice world health question, then we might like to understand if

H0: People never learn these particular topics and their responses are simply equivalent to random
      guesses.

HA: People have knowledge that helps them do better than random guessing, or perhaps, they have
       false knowledge that leads them to actually do worse than random guessing.

These competing ideas are called hypotheses. We call H0 the null hypothesis and HA the alternative
hypothesis. When there is a subscript 0 like in H0, data scientists pronounce it as “nought” (e.g. H0
is pronounced “H-nought”).


  NULL AND ALTERNATIVE HYPOTHESES
  The null hypothesis (H0) often represents a skeptical perspective or a claim to be tested.
  The alternative hypothesis (HA) represents an alternative claim under consideration and is
  often represented by a range of possible parameter values.

  Our job as data scientists is to play the role of a skeptic: before we buy into the alternative
  hypothesis, we need to see strong supporting evidence.


    The null hypothesis often represents a skeptical position or a perspective of “no diﬀerence”. In
our ﬁrst example, we’ll consider whether the typical person does any diﬀerent than random guessing
on Roslings’ question about infant vaccinations.
    The alternative hypothesis generally represents a new or stronger perspective. In the case of
the question about infant vaccinations, it would certainly be interesting to learn whether people do
better than random guessing, since that would mean that the typical person knows something about
world health statistics.  It would also be very interesting if we learned that people do worse than
random guessing, which would suggest people believe incorrect information about world health.
    The hypothesis testing framework is a very general tool, and we often use it without a second
thought.  If a person makes a somewhat unbelievable claim, we are initially skeptical. However,
if there is suﬃcient evidence that supports the claim, we set aside our skepticism and reject the null
hypothesis in favor of the alternative. The hallmarks of hypothesis testing are also found in the
US court system.



  13The correct answer is (c): 80% of the world’s 1 year olds have been vaccinated against some disease.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 190

190                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE



           GUIDED PRACTICE 5.17
         A US court considers two possible claims about a defendant: she is either innocent or guilty. If we
                set these claims up in a hypothesis framework, which would be the null hypothesis and which the
               alternative?14

                   Jurors examine the evidence to see whether it convincingly shows a defendant is guilty. Even
                      if the jurors leave unconvinced of guilt beyond a reasonable doubt, this does not mean they believe
              the defendant is innocent. This is also the case with hypothesis testing: even if we fail to reject the
                null hypothesis, we typically do not accept the null hypothesis as true. Failing to ﬁnd strong evidence
                for the alternative hypothesis is not equivalent to accepting the null hypothesis.
             When considering Roslings’ question about infant vaccination, the null hypothesis represents
              the notion that the people we will be considering – college-educated adults – are as accurate as
            random guessing. That is, the proportion p of respondents who pick the correct answer, that 80%
                of 1 year olds have been vaccinated against some disease, is about 33.3% (or 1-in-3 if wanting to
             be perfectly precise). The alternative hypothesis is that this proportion is something other than
              33.3%. While it’s helpful to write these hypotheses in words, it can be useful to write them using
             mathematical notation:

            H0: p = 0.333

           HA:  p̸ = 0.333

              In this hypothesis setup, we want to make a conclusion about the population parameter p. The
              value we are comparing the parameter to is called the null value, which in this case is 0.333. It’s
           common to label the null value with the same symbol as the parameter but with a subscript ‘0’.
            That is, in this case, the null value is p0 = 0.333 (pronounced “p-nought equals 0.333”).


          EXAMPLE 5.18
                 It may seem impossible that the proportion of people who get the correct answer is exactly 33.3%.
                   If we don’t believe the null hypothesis, should we simply reject it?

             No. While we may not buy into the notion that the proportion is exactly 33.3%, the hypothesis
               testing framework requires that there be strong evidence before we reject the null hypothesis and
              conclude something more interesting.

              After all, even if we don’t believe the proportion is exactly 33.3%, that doesn’t really tell us anything
                useful! We would still be stuck with the original question: do people do better or worse than random
              guessing on Roslings’ question? Without data that strongly points in one direction or the other, it
                   is both uninteresting and pointless to reject H0.


           GUIDED PRACTICE 5.19
             Another example of a real-world hypothesis testing situation is evaluating whether a new drug is
               better or worse than an existing drug at treating a particular disease. What should we use for the
                null and alternative hypotheses in this case?15





                 14The jury considers whether the evidence is so convincing (strong) that there is no reasonable doubt regarding the
                 person’s guilt; in such a case, the jury rejects innocence (the null hypothesis) and concludes the defendant is guilty
                  (alternative hypothesis).
                 15The null hypothesis (H0) in this case is the declaration of no diﬀerence: the drugs are equally eﬀective. The
                  alternative hypothesis (HA) is that the new drug performs diﬀerently than the original, i.e.  it could perform better
                 or worse.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 191

5.3. HYPOTHESIS TESTING FOR A PROPORTION                                                191


5.3.2  Testing hypotheses using conﬁdence intervals

   We will use the rosling responses data set to evaluate the hypothesis test evaluating whether
college-educated adults who get the question about infant vaccination correct is diﬀerent from 33.3%.
This data set summarizes the answers of 50 college-educated adults. Of these 50 adults, 24% of
respondents got the question correct that 80% of 1 year olds have been vaccinated against some
disease.
   Up until now, our discussion has been philosophical. However, now that we have data, we might
ask ourselves: does the data provide strong evidence that the proportion of all college-educated adults
who would answer this question correctly is diﬀerent than 33.3%?
   We learned in Section 5.1 that there is ﬂuctuation from one sample to another, and it is
unlikely that our sample proportion,  ˆp, will exactly equal p, but we want to make a conclusion
about p. We have a nagging concern:  is this deviation of 24% from 33.3% simply due to chance,
or does the data provide strong evidence that the population proportion is diﬀerent from 33.3%?
     In Section 5.2, we learned how to quantify the uncertainty in our estimate using conﬁdence
intervals. The same method for measuring variability can be useful for the hypothesis test.


EXAMPLE 5.20
Check whether it is reasonable to construct a conﬁdence interval for p using the sample data, and if
so, construct a 95% conﬁdence interval.

The conditions are met for ˆp to be approximately normal: the data come from a simple random
sample (satisﬁes independence), and nˆp = 12 and n(1 −ˆp) = 38 are both at least 10 (success-failure
condition).

To construct the conﬁdence interval, we will need to identify the point estimate (ˆp = 0.24), the critical
value for the 95% conﬁdence level (z⋆= 1.96), and the standard error of ˆp (SEˆp = p ˆp(1 −ˆp)/n =
0.060). With those pieces, the conﬁdence interval for p can be constructed:

                                                            ˆp ± z⋆× SEˆp
                                       0.24 ± 1.96 × 0.060

                                          (0.122, 0.358)

We are 95% conﬁdent that the proportion of all college-educated adults to correctly answer this
particular question about infant vaccination is between 12.2% and 35.8%.

    Because the null value in the hypothesis test is p0 = 0.333, which falls within the range of
plausible values from the conﬁdence interval, we cannot say the null value is implausible.16 That
is, the data do not provide suﬃcient evidence to reject the notion that the performance of collegeeducated adults was diﬀerent than random guessing, and we do not reject the null hypothesis, H0.


EXAMPLE 5.21
Explain why we cannot conclude that college-educated adults simply guessed on the infant vaccination question.

While we failed to reject H0, that does not necessarily mean the null hypothesis is true. Perhaps
there was an actual diﬀerence, but we were not able to detect it with the relatively small sample
of 50.



  DOUBLE NEGATIVES CAN SOMETIMES BE USED IN STATISTICS
  In many statistical explanations, we use double negatives. For instance, we might say that the
  null hypothesis is not implausible or we failed to reject the null hypothesis. Double negatives
  are used to communicate that while we are not rejecting a position, we are also not saying it is
  correct.

  16Arguably this method is slightly imprecise. As we’ll see in a few pages, the standard error is often computed
slightly diﬀerently in the context of a hypothesis test for a proportion.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 192

192                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE



           GUIDED PRACTICE 5.22
               Let’s move onto a second question posed by the Roslings:

                  There are 2 billion children in the world today aged 0-15 years old, how many children
                       will there be in year 2100 according to the United Nations?

                        a. 4 billion.
                          b. 3 billion.
                          c. 2 billion.

              Set up appropriate hypotheses to evaluate whether college-educated adults are better than random
              guessing on this question. Also, see if you can guess the correct answer before checking the answer
                in the footnote!17



           GUIDED PRACTICE 5.23
             This time we took a larger sample of 228 college-educated adults, 34 (14.9%) selected the correct
             answer to the question in Guided Practice 5.22: 2 billion. Can we model the sample proportion
              using a normal distribution and construct a conﬁdence interval?18




          EXAMPLE 5.24
           Compute a 95% conﬁdence interval for the fraction of college-educated adults who answered the
               children-in-2100 question correctly, and evaluate the hypotheses in Guided Practice 5.22.

           To compute the standard error, we’ll again use ˆp in place of p for the calculation:

                     r ˆp(1 −ˆp) r 0.149(1 −0.149)
                                     SEˆp =       =           = 0.024
                                       n              228

              In Guided Practice 5.23, we found that ˆp can be modeled using a normal distribution, which ensures
             a 95% conﬁdence interval may be accurately constructed as

                                                ˆp ± z⋆× SE →   0.149 ± 1.96 × 0.024 →   (0.103, 0.195)

             Because the null value, p0 = 0.333, is not in the conﬁdence interval, a population proportion of 0.333
                   is implausible and we reject the null hypothesis. That is, the data provide statistically signiﬁcant
              evidence that the actual proportion of college adults who get the children-in-2100 question correct
                   is diﬀerent from random guessing. Because the entire 95% conﬁdence interval is below 0.333, we can
              conclude college-educated adults do worse than random guessing on this question.

           One subtle consideration is that we used a 95% conﬁdence interval. What if we had used a 99%
             conﬁdence level? Or even a 99.9% conﬁdence level?  It’s possible to come to a diﬀerent conclusion
                      if using a diﬀerent conﬁdence level.  Therefore, when we make a conclusion based on conﬁdence
                interval, we should also be sure it is clear what conﬁdence level we used.


               The worse-than-random performance on this last question is not a ﬂuke: there are many such
             world health questions where people do worse than random guessing. In general, the answers suggest
              that people tend to be more pessimistic about progress than reality suggests. This topic is discussed
                in much greater detail in the Roslings’ book, Factfulness.

                 17The appropriate hypotheses are:
                H0: the proportion who get the answer correct is the same as random guessing: 1-in-3, or p = 0.333.
              HA: the proportion who get the answer correct is diﬀerent than random guessing, p̸ = 0.333.
               The correct answer to the question is 2 billion. While the world population is projected to increase, the average
                age is also expected to rise. That is, the majority of the population growth will happen in older age groups, meaning
                people are projected to live longer in the future across much of the world.
               18We check both conditions, which are satisﬁed, so it is reasonable to use a normal distribution for ˆp:
              Independence. Since the data are from a simple random sample, the observations are independent.
                Success-failure. We’ll use ˆp in place of p to check: nˆp = 34 and n(1 −ˆp) = 194. Both are greater than 10, so the
                   success-failure condition is satisﬁed.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 193

5.3. HYPOTHESIS TESTING FOR A PROPORTION                                                193


5.3.3  Decision errors

     Hypothesis tests are not ﬂawless: we can make an incorrect decision in a statistical hypothesis
test based on the data. For example, in the court system innocent people are sometimes wrongly
convicted and the guilty sometimes walk free. One key distinction with statistical hypothesis tests
is that we have the tools necessary to probabilistically quantify how often we make errors in our
conclusions.
     Recall that there are two competing hypotheses: the null and the alternative. In a hypothesis
test, we make a statement about which one might be true, but we might choose incorrectly. There
are four possible scenarios, which are summarized in Figure 5.8.

                                          Test conclusion
                               do not reject H0   reject H0 in favor of HA
                   H0 true        okay         Type 1 Error
             Truth
                HA true  Type 2 Error            okay

                    Figure 5.8: Four diﬀerent scenarios for hypothesis tests.

   A Type 1 Error is rejecting the null hypothesis when H0 is actually true. A Type 2 Error
is failing to reject the null hypothesis when the alternative is actually true.


GUIDED PRACTICE 5.25
In a US court, the defendant is either innocent (H0) or guilty (HA). What does a Type 1 Error
represent in this context? What does a Type 2 Error represent? Figure 5.8 may be useful.19




EXAMPLE 5.26
How could we reduce the Type 1 Error rate in US courts? What inﬂuence would this have on the
Type 2 Error rate?

To lower the Type 1 Error rate, we might raise our standard for conviction from “beyond a reasonable
doubt” to “beyond a conceivable doubt” so fewer people would be wrongly convicted. However, this
would also make it more diﬃcult to convict the people who are actually guilty, so we would make
more Type 2 Errors.


GUIDED PRACTICE 5.27
How could we reduce the Type 2 Error rate in US courts? What inﬂuence would this have on the
Type 1 Error rate?20


     Exercises 5.25-5.27 provide an important lesson:  if we reduce how often we make one type of
error, we generally make more of the other type.
     Hypothesis testing is built around rejecting or failing to reject the null hypothesis. That is, we
do not reject H0 unless we have strong evidence. But what precisely does strong evidence mean? As
a general rule of thumb, for those cases where the null hypothesis is actually true, we do not want
to incorrectly reject H0 more than 5% of the time. This corresponds to a signiﬁcance level of
0.05. That is, if the null hypothesis is true, the signiﬁcance level indicates how often the data lead
us to incorrectly reject H0. We often write the signiﬁcance level using α (the Greek letter alpha):
α = 0.05. We discuss the appropriateness of diﬀerent signiﬁcance levels in Section 5.3.5.


   19If the court makes a Type 1 Error, this means the defendant is innocent (H0 true) but wrongly convicted. Note
that a Type 1 Error is only possible if we’ve rejected the null hypothesis.
 A Type 2 Error means the court failed to reject H0 (i.e. failed to convict the person) when she was in fact guilty
(HA true). Note that a Type 2 Error is only possible if we have failed to reject the null hypothesis.
  20To lower the Type 2 Error rate, we want to convict more guilty people. We could lower the standards for
conviction from “beyond a reasonable doubt” to “beyond a little doubt”. Lowering the bar for guilt will also result
in more wrongful convictions, raising the Type 1 Error rate.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 194

194                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE


                          If we use a 95% conﬁdence interval to evaluate a hypothesis test and the null hypothesis happens
               to be true, we will make an error whenever the point estimate is at least 1.96 standard errors away
             from the population parameter. This happens about 5% of the time (2.5% in each tail). Similarly,
              using a 99% conﬁdence interval to evaluate a hypothesis is equivalent to a signiﬁcance level of
          α = 0.01.
            A conﬁdence interval is very helpful in determining whether or not to reject the null hypothesis.
             However, the conﬁdence interval approach isn’t always sustainable.  In several sections, we will
              encounter situations where a conﬁdence interval cannot be constructed. For example, if we wanted
               to evaluate the hypothesis that several proportions are equal, it isn’t clear how to construct and
            compare many conﬁdence intervals altogether.
                Next we will introduce a statistic called the p-value to help us expand our statistical toolkit,
             which will enable us to both better understand the strength of evidence and work in more complex
             data scenarios in later sections.


            5.3.4  Formal testing using p-values

               The p-value is a way of quantifying the strength of the evidence against the null hypothesis
            and in favor of the alternative hypothesis. Statistical hypothesis testing typically uses the p-value
            method rather than making a decision based on conﬁdence intervals.


              P-VALUE
             The p-value is the probability of observing data at least as favorable to the alternative hy-
                 pothesis as our current data set, if the null hypothesis were true. We typically use a summary
                    statistic of the data, in this section the sample proportion, to help compute the p-value and
                 evaluate the hypotheses.




          EXAMPLE 5.28
           Pew Research asked a random sample of 1000 American adults whether they supported the increased
              usage of coal to produce energy.  Set up hypotheses to evaluate whether a majority of American
               adults support or oppose the increased usage of coal.

           The uninteresting result is that there is no majority either way: half of Americans support and the
              other half oppose expanding the use of coal to produce energy. The alternative hypothesis would be
              that there is a majority support or oppose (though we do not known which one!) expanding the use
                of coal. If p represents the proportion supporting, then we can write the hypotheses as

            H0: p = 0.5

           HA:  p̸ = 0.5

              In this case, the null value is p0 = 0.5.


             When evaluating hypotheses for proportions using the p-value method, we will slightly modify
           how we check the success-failure condition and compute the standard error for the single proportion
                case. These changes aren’t dramatic, but pay close attention to how we use the null value, p0.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 195

5.3. HYPOTHESIS TESTING FOR A PROPORTION                                                195



EXAMPLE 5.29
Pew Research’s sample show that 37% of American adults support increased usage of coal. We now
wonder, does 37% represent a real diﬀerence from the null hypothesis of 50%? What would the
sampling distribution of ˆp look like if the null hypothesis were true?

If the null hypothesis were true, the population proportion would be the null value, 0.5. We previously learned that the sampling distribution of ˆp will be normal when two conditions are met:


Independence. The poll was based on a simple random sample, so independence is satisﬁed.

Success-failure. Based on the poll’s sample size of n = 1000, the success-failure condition is met,
      since

                   H0                                 H0
              np = 1000 × 0.5 = 500        n(1 −p) = 1000 × (1 −0.5) = 500

      are both at least 10. Note that the success-failure condition was checked using the null value,
      p0 = 0.5; this is the ﬁrst procedural diﬀerence from conﬁdence intervals.

If the null hypothesis were true, the sampling distribution indicates that a sample proportion based
on n = 1000 observations would be normally distributed. Next, we can compute the standard error,
where we will again use the null value p0 = 0.5 in the calculation:

              r p(1 −p)   H0 r 0.5 × (1 −0.5)
                      SEˆp =        =            = 0.016
                           n                 1000

This marks the other procedural diﬀerence from conﬁdence intervals: since the sampling distribution is determined under the null proportion, the null value p0 was used for the proportion in the
calculation rather than ˆp.

Ultimately,  if the null hypothesis were true, then the sample proportion should follow a normal
distribution with mean 0.5 and a standard error of 0.016. This distribution is shown in Figure 5.9.



                Observed p^ = 0.37



                        0.37                  0.50

        Figure 5.9: If the null hypothesis were true, this normal distribution describes the
         distribution of ˆp.



  CHECKING SUCCESS-FAILURE AND COMPUTING SEˆP FOR A HYPOTHESIS TEST
  When using the p-value method to evaluate a hypothesis test, we check the conditions for ˆp and
  construct the standard error using the null value, p0, instead of using the sample proportion.

  In a hypothesis test with a p-value, we are supposing the null hypothesis is true, which is a
  diﬀerent mindset than when we compute a conﬁdence interval. This is why we use p0 instead
   of ˆp when we check conditions and compute the standard error in this context.


   When we identify the sampling distribution under the null hypothesis, it has a special name:
the null distribution. The p-value represents the probability of the observed ˆp, or a ˆp that is more
extreme, if the null hypothesis were true. To ﬁnd the p-value, we generally ﬁnd the null distribution,
and then we ﬁnd a tail area in that distribution corresponding to our point estimate.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 196

196                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE



          EXAMPLE 5.30
                   If the null hypothesis were true, determine the chance of ﬁnding ˆp at least as far into the tails as
               0.37 under the null distribution, which is a normal distribution with mean µ = 0.5 and SE = 0.016.

             This is a normal probability problem where x = 0.37. First, we draw a simple graph to represent
              the situation, similar to what is shown in Figure 5.9. Since ˆp is so far out in the tail, we know the
                  tail area is going to be very small. To ﬁnd it, we start by computing the Z-score using the mean of
               0.5 and the standard error of 0.016:

                                                        0.37 −0.5
                                 Z =       = −8.125
                                                         0.016

         We can use software to ﬁnd the tail area: 2.2 × 10−16 (0.00000000000000022).  If using the normal
               probability table in Appendix C.1, we’d ﬁnd that Z = −8.125 is oﬀthe table, so we would use the
               smallest area listed: 0.0002.

           The potential  ˆp’s in the upper tail beyond 0.63, which are shown in Figure 5.10, also represent
              observations at least as extreme as the observed value of 0.37. To account for these values that are
                also more extreme under the hypothesis setup, we double the lower tail to get an estimate of the
               p-value: 4.4 × 10−16 (or if using the table method, 0.0004).

           The p-value represents the probability of observing such an extreme sample proportion by chance,
                      if the null hypothesis were true.



                                            Tail Area for p^                       Equally unlikely if H0 is true


                                      0.37                  0.50                  0.63

                      Figure 5.10:  If H0 were true, then the values above 0.63 are just as unlikely as
                       values below 0.37.



          EXAMPLE 5.31
          How should we evaluate the hypotheses using the p-value of 4.4×10−16? Use the standard signiﬁcance
                 level of α = 0.05.

                   If the null hypothesis were true, there’s only an incredibly small chance of observing such an extreme
               deviation of ˆp from 0.5. This means one of the following must be true:


                    1. The null hypothesis is true, and we just happened to get observe something so extreme that
                   only happens about once in every 23 quadrillion times (1 quadrillion = 1 million × 1 billion).

                    2. The alternative hypothesis is true, which would be consistent with observing a sample propor-
                     tion far from 0.5.


           The ﬁrst scenario is laughably improbable, while the second scenario seems much more plausible.

              Formally, when we evaluate a hypothesis test, we compare the p-value to the signiﬁcance level, which
                in this case is α = 0.05. Since the p-value is less than α, we reject the null hypothesis. That is,
              the data provide strong evidence against H0. The data indicate the direction of the diﬀerence: a
              majority of Americans do not support expanding the use of coal-powered energy.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 197

5.3. HYPOTHESIS TESTING FOR A PROPORTION                                                197



  COMPARE THE P-VALUE TO α TO EVALUATE H0H0H0
  When the p-value is less than the signiﬁcance level, α, reject H0. We would report a conclusion
  that the data provide strong evidence supporting the alternative hypothesis.

  When the p-value is greater than α, do not reject H0, and report that we do not have suﬃcient
  evidence to reject the null hypothesis.

  In either case, it is important to describe the conclusion in the context of the data.




GUIDED PRACTICE 5.32
Do a majority of Americans support or oppose nuclear arms reduction?  Set up hypotheses to
evaluate this question.21




EXAMPLE 5.33
A simple random sample of 1028 US adults in March 2013 show that 56% support nuclear arms
reduction. Does this provide convincing evidence that a majority of Americans supported nuclear
arms reduction at the 5% signiﬁcance level?

First, check conditions:


Independence. The poll was of a simple random sample of US adults, meaning the observations
      are independent.

Success-failure. In a one-proportion hypothesis test, this condition is checked using the null pro-
      portion, which is p0 = 0.5 in this context: np0 = n(1 −p0) = 1028 × 0.5 = 514 ≥10.

With these conditions veriﬁed, we can model ˆp using a normal model.

Next the standard error can be computed. The null value p0 is used again here, because this is a
hypothesis test for a single proportion.

               r p0(1 −p0) r 0.5(1 −0.5)
                        SEˆp =        =         = 0.0156
                             n            1028

Based on the normal model, the test statistic can be computed as the Z-score of the point estimate:

                           point estimate −null value    0.56 −0.50
               Z =                =       = 3.85
                         SE                 0.0156

It’s generally helpful to draw null distribution and the tail areas of interest for computing the p-value:


                         lower tail                 upper tail


                                                  0.5          0.56


The upper tail area is about 0.0001, and we double this tail area to get the p-value: 0.0002. Because
the p-value is smaller than 0.05, we reject H0. The poll provides convincing evidence that a majority
of Americans supported nuclear arms reduction eﬀorts in March 2013.





  21We would like to understand if a majority supports or opposes, or ultimately, if there is no diﬀerence. If p is the
proportion of Americans who support nuclear arms reduction, then H0: p = 0.50 and HA:  p̸ = 0.50.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 198

198                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE



             HYPOTHESIS TESTING FOR A SINGLE PROPORTION
              Once you’ve determined a one-proportion hypothesis test is the correct procedure, there are
                 four steps to completing the test:

              Prepare. Identify the parameter of interest, list hypotheses, identify the signiﬁcance level, and
                        identify ˆp and n.

             Check. Verify conditions to ensure ˆp is nearly normal under H0. For one-proportion hypothesis
                          tests, use the null value to check the success-failure condition.

               Calculate.  If the conditions hold, compute the standard error, again using p0, compute the
                        Z-score, and identify the p-value.

              Conclude. Evaluate the hypothesis test by comparing the p-value to α, and provide a conclu-
                       sion in the context of the problem.



            5.3.5  Choosing a signiﬁcance level

                 Choosing a signiﬁcance level for a test is important in many contexts, and the traditional level
                   is α = 0.05. However, it can be helpful to adjust the signiﬁcance level based on the application.
         We may select a level that is smaller or larger than 0.05 depending on the consequences of any
               conclusions reached from the test.
                          If making a Type 1 Error is dangerous or especially costly, we should choose a small signiﬁcance
                 level (e.g. 0.01). Under this scenario we want to be very cautious about rejecting the null hypothesis,
               so we demand very strong evidence favoring HA before we would reject H0.
                          If a Type 2 Error is relatively more dangerous or much more costly than a Type 1 Error, then
           we might choose a higher signiﬁcance level (e.g. 0.10). Here we want to be cautious about failing to
                reject H0 when the alternative hypothesis is actually true.
                    Additionally, if the cost of collecting data is small relative to the cost of a Type 2 Error, then
                    it may also be a good strategy to collect more data. Under this strategy, the Type 2 Error can be
             reduced while not aﬀecting the Type 1 Error rate. Of course, collecting extra data is often costly,
               so there is typically a cost-beneﬁt analysis to be considered.


          EXAMPLE 5.34
         A car manufacturer is considering switching to a new, higher quality piece of equipment that con-
               structs vehicle door hinges. They ﬁgure that they will save money in the long run if this new machine
             produces hinges that have ﬂaws less than 0.2% of the time. However, if the hinges are ﬂawed more
             than 0.2% of the time, they wouldn’t get a good enough return-on-investment from the new piece
                of equipment, and they would lose money. Is there good reason to modify the signiﬁcance level in
              such a hypothesis test?

           The null hypothesis would be that the rate of ﬂawed hinges is 0.2%, while the alternative is that it
              the rate is diﬀerent than 0.2%. This decision is just one of many that have a marginal impact on
              the car and company. A signiﬁcance level of 0.05 seems reasonable since neither a Type 1 or Type 2
              Error should be dangerous or (relatively) much more expensive.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 199

5.3. HYPOTHESIS TESTING FOR A PROPORTION                                                199



EXAMPLE 5.35
The same car manufacturer is considering a slightly more expensive supplier for parts related to
safety, not door hinges. If the durability of these safety components is shown to be better than the
current supplier, they will switch manufacturers.  Is there good reason to modify the signiﬁcance
level in such an evaluation?

The null hypothesis would be that the suppliers’ parts are equally reliable. Because safety is involved,
the car company should be eager to switch to the slightly more expensive manufacturer (reject H0),
even if the evidence of increased safety is only moderately strong. A slightly larger signiﬁcance level,
such as α = 0.10, might be appropriate.


GUIDED PRACTICE 5.36
A part inside of a machine is very expensive to replace. However, the machine usually functions
properly even if this part is broken, so the part is replaced only if we are extremely certain it is
broken based on a series of measurements.  Identify appropriate hypotheses for this test (in plain
language) and suggest an appropriate signiﬁcance level.22




 WHY IS 0.05 THE DEFAULT?
  The α = 0.05 threshold is most common.  But why? Maybe the standard level should be
  smaller, or perhaps larger. If you’re a little puzzled, you’re reading with an extra critical eye –
  good job! We’ve made a 5-minute task to help clarify why 0.05:

                                www.openintro.org/why05




5.3.6  Statistical signiﬁcance versus practical signiﬁcance

   When the sample size becomes larger, point estimates become more precise and any real diﬀerences in the mean and null value become easier to detect and recognize. Even a very small diﬀerence
would likely be detected if we took a large enough sample. Sometimes researchers will take such large
samples that even the slightest diﬀerence is detected, even diﬀerences where there is no practical
value. In such cases, we still say the diﬀerence is statistically signiﬁcant, but it is not practically signiﬁcant. For example, an online experiment might identify that placing additional ads on
a movie review website statistically signiﬁcantly increases viewership of a TV show by 0.001%, but
this increase might not have any practical value.
    One role of a data scientist in conducting a study often includes planning the size of the study.
The data scientist might ﬁrst consult experts or scientiﬁc literature to learn what would be the
smallest meaningful diﬀerence from the null value. She also would obtain other information, such
as a very rough estimate of the true proportion p, so that she could roughly estimate the standard
error. From here, she can suggest a sample size that is suﬃciently large that,  if there is a real
diﬀerence that is meaningful, we could detect it. While larger sample sizes may still be used, these
calculations are especially helpful when considering costs or potential risks, such as possible health
impacts to volunteers in a medical study.





  22Here the null hypothesis is that the part is not broken, and the alternative is that it is broken. If we don’t have
suﬃcient evidence to reject H0, we would not replace the part.  It sounds like failing to ﬁx the part if it is broken
(H0 false, HA true) is not very problematic, and replacing the part is expensive. Thus, we should require very strong
evidence against H0 before we replace the part. Choose a small signiﬁcance level, such as α = 0.01.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 200

200                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE


            5.3.7  One-sided hypothesis tests (special topic)

                So far we’ve only considered what are called two-sided hypothesis tests, where we care about
               detecting whether p is either above or below some null value p0. There is a second type of hypothesis
                test called a one-sided hypothesis test. For a one-sided hypothesis test, the hypotheses take one
                of the following forms:

                    1. There’s only value in detecting if the population parameter is less than some value p0. In this
                      case, the alternative hypothesis is written as p < p0 for some null value p0.

                    2. There’s only value in detecting if the population parameter is more than some value p0: In this
                      case, the alternative hypothesis is written as p > p0.

             While we adjust the form of the alternative hypothesis, we continue to write the null hypothesis
              using an equals-sign in the one-sided hypothesis test case.
                   In the entire hypothesis testing procedure, there is only one diﬀerence in evaluating a one-
               sided hypothesis test vs a two-sided hypothesis test: how to compute the p-value. In a one-sided
              hypothesis test, we compute the p-value as the tail area in the direction of the alternative hypothesis
                only, meaning it is represented by a single tail area. Herein lies the reason why one-sided tests are
             sometimes interesting:  if we don’t have to double the tail area to get the p-value, then the p-value
                   is smaller and the level of evidence required to identify an interesting ﬁnding in the direction of the
               alternative hypothesis goes down. However, one-sided tests aren’t all sunshine and rainbows: the
             heavy price paid is that any interesting ﬁndings in the opposite direction must be disregarded.


          EXAMPLE 5.37
              In Section 1.1, we encountered an example where doctors were interested in determining whether
               stents would help people who had a high risk of stroke. The researchers believed the stents would
               help. Unfortunately, the data showed the opposite: patients who received stents actually did worse.
         Why was using a two-sided test so important in this context?

              Before the study, researchers had reason to believe that stents would help patients since existing
               research suggested stents helped in patients with heart attacks. It would surely have been tempting
               to use a one-sided test in this situation, and had they done this, they would have limited their ability
               to identify potential harm to patients.


                Example 5.37 highlights that using a one-sided hypothesis creates a risk of overlooking data
              supporting the opposite conclusion. We could have made a similar error when reviewing the Roslings’
              question data this section; if we had a pre-conceived notion that college-educated people wouldn’t do
             worse than random guessing and so used a one-sided test, we would have missed the really interesting
             ﬁnding that many people have incorrect knowledge about global public health.
             When might a one-sided test be appropriate to use? Very rarely. Should you ever ﬁnd yourself
               considering using a one-sided test, carefully answer the following question:

               What would I, or others, conclude if the data happens to go clearly in the opposite direc-
                     tion than my alternative hypothesis?

                    If you or others would ﬁnd any value in making a conclusion about the data that goes in the
              opposite direction of a one-sided test, then a two-sided hypothesis test should actually be used.
             These considerations can be subtle, so exercise caution. We will only apply two-sided tests in the
                rest of this book.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 201

5.3. HYPOTHESIS TESTING FOR A PROPORTION                                                201



EXAMPLE 5.38
Why can’t we simply run a one-sided test that goes in the direction of the data?

We’ve been building a careful framework that controls for the Type 1 Error, which is the signiﬁcance
level α in a hypothesis test. We’ll use the α = 0.05 below to keep things simple.

Imagine we could pick the one-sided test after we saw the data. What will go wrong?

   • If ˆp is smaller than the null value, then a one-sided test where p < p0 would mean that any
      observation in the lower 5% tail of the null distribution would lead to us rejecting H0.

   • If ˆp is larger than the null value, then a one-sided test where p > p0 would mean that any
      observation in the upper 5% tail of the null distribution would lead to us rejecting H0.

Then if H0 were true, there’s a 10% chance of being in one of the two tails, so our testing error is
actually α = 0.10, not 0.05. That is, not being careful about when to use one-sided tests eﬀectively
undermines the methods we’re working so hard to develop and utilize.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 202

202                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE


           Exercises


               5.15  Identify hypotheses, Part I. Write the null and alternative hypotheses in words and then symbols for
               each of the following situations.

                (a) A tutoring company would like to understand if most students tend to improve their grades (or not)
                      after they use their services. They sample 200 of the students who used their service in the past year
                and ask them if their grades have improved or declined from the previous year.
                (b) Employers at a ﬁrm are worried about the eﬀect of March Madness, a basketball championship held each
                    spring in the US, on employee productivity. They estimate that on a regular business day employees
                 spend on average 15 minutes of company time checking personal email, making personal phone calls,
                       etc. They also collect data on how much company time employees spend on such non-business activities
                   during March Madness. They want to determine if these data provide convincing evidence that employee
                    productivity changed during March Madness.

               5.16  Identify hypotheses, Part II. Write the null and alternative hypotheses in words and using symbols
                  for each of the following situations.

                (a) Since 2008, chain restaurants in California have been required to display calorie counts of each menu
                    item. Prior to menus displaying calorie counts, the average calorie intake of diners at a restaurant was
                  1100 calories. After calorie counts started to be displayed on menus, a nutritionist collected data on the
                number of calories consumed at this restaurant from a random sample of diners. Do these data provide
                   convincing evidence of a diﬀerence in the average calorie intake of a diners at this restaurant?
                (b) The state of Wisconsin would like to understand the fraction of its adult residents that consumed alcohol
                     in the last year, speciﬁcally if the rate is diﬀerent from the national rate of 70%. To help them answer this
                    question, they conduct a random sample of 852 residents and ask them about their alcohol consumption.

               5.17  Online communication. A study suggests that 60% of college student spend 10 or more hours per
             week communicating with others online. You believe that this is incorrect and decide to collect your own
              sample for a hypothesis test. You randomly sample 160 students from your dorm and ﬁnd that 70% spent
              10 or more hours a week communicating with others online. A friend of yours, who oﬀers to help you with
               the hypothesis test, comes up with the following set of hypotheses. Indicate any errors you see.

                                              H0 : ˆp < 0.6
                                       HA : ˆp > 0.7

               5.18  Married at 25. A study suggests that the 25% of 25 year olds have gotten married. You believe that
                 this is incorrect and decide to collect your own sample for a hypothesis test. From a random sample of 25
               year olds in census data with size 776, you ﬁnd that 24% of them are married. A friend of yours oﬀers
                to help you with setting up the hypothesis test and comes up with the following hypotheses. Indicate any
                 errors you see.

                                             H0 : ˆp = 0.24
                                       HA : ˆp̸ = 0.24

               5.19  Cyberbullying rates. Teens were surveyed about cyberbullying, and 54% to 64% reported experienc-
                ing cyberbullying (95% conﬁdence interval).23 Answer the following questions based on this interval.

                (a) A newspaper claims that a majority of teens have experienced cyberbullying.  Is this claim supported
                 by the conﬁdence interval? Explain your reasoning.
                (b) A researcher conjectured that 70% of teens have experienced cyberbullying. Is this claim supported by
                   the conﬁdence interval? Explain your reasoning.
                 (c) Without actually calculating the interval, determine if the claim of the researcher from part (b) would
                 be supported based on a 90% conﬁdence interval?





                23Pew Research Center, A Majority of Teens Have Experienced Some Form of Cyberbullying. September 27, 2018.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 203

5.3. HYPOTHESIS TESTING FOR A PROPORTION                                                203


5.20  Waiting at an ER, Part II. Exercise 5.11 provides a 95% conﬁdence interval for the mean waiting time
at an emergency room (ER) of (128 minutes, 147 minutes). Answer the following questions based on this
interval.

(a) A local newspaper claims that the average waiting time at this ER exceeds 3 hours.  Is this claim
    supported by the conﬁdence interval? Explain your reasoning.
(b) The Dean of Medicine at this hospital claims the average wait time is 2.2 hours. Is this claim supported
    by the conﬁdence interval? Explain your reasoning.
(c) Without actually calculating the interval, determine if the claim of the Dean from part (b) would be
    supported based on a 99% conﬁdence interval?

5.21  Minimum wage, Part I. Do a majority of US adults believe raising the minimum wage will help the
economy, or is there a majority who do not believe this? A Rasmussen Reports survey of 1,000 US adults
found that 42% believe it will help the economy.24 Conduct an appropriate hypothesis test to help answer
the research question.

5.22  Getting enough sleep. 400 students were randomly sampled from a large university, and 289 said
they did not get enough sleep. Conduct a hypothesis test to check whether this represents a statistically
signiﬁcant diﬀerence from 50%, and use a signiﬁcance level of 0.01.

5.23  Working backwards, Part I. You are given the following hypotheses:

                                  H0 : p = 0.3
                             HA : p̸ = 0.3

We know the sample size is 90. For what sample proportion would the p-value be equal to 0.05? Assume
that all conditions necessary for inference are satisﬁed.

5.24  Working backwards, Part II. You are given the following hypotheses:

                                  H0 : p = 0.9
                             HA : p̸ = 0.9

We know that the sample size is 1,429. For what sample proportion would the p-value be equal to 0.01?
Assume that all conditions necessary for inference are satisﬁed.

5.25  Testing for Fibromyalgia. A patient named Diana was diagnosed with Fibromyalgia, a long-term
syndrome of body pain, and was prescribed anti-depressants. Being the skeptic that she is, Diana didn’t
initially believe that anti-depressants would help her symptoms. However after a couple months of being on
the medication she decides that the anti-depressants are working, because she feels like her symptoms are
in fact getting better.

(a) Write the hypotheses in words for Diana’s skeptical position when she started taking the anti-depressants.
(b) What is a Type 1 Error in this context?
(c) What is a Type 2 Error in this context?

5.26  Which is higher? In each part below, there is a value of interest and two scenarios (I and II). For
each part, report if the value of interest is larger under scenario I, scenario II, or whether the value is equal
under the scenarios.

(a) The standard error of ˆp when (I) n = 125 or (II) n = 500.
(b) The margin of error of a conﬁdence interval when the conﬁdence level is (I) 90% or (II) 80%.
(c) The p-value for a Z-statistic of 2.5 calculated based on a (I) sample with n = 500 or based on a (II) sample
    with n = 1000.
(d) The probability of making a Type 2 Error when the alternative hypothesis is true and the signiﬁcance
     level is (I) 0.05 or (II) 0.10.





  24Rasmussen Reports survey, Most Favor Minimum Wage of $10.50 Or Higher, April 16, 2019.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 204

204                                   CHAPTER 5. FOUNDATIONS FOR INFERENCE


       Chapter exercises



               5.27  Relaxing after work. The General Social Survey asked the question: “After an average work day,
              about how many hours do you have to relax or pursue activities that you enjoy?” to a random sample of
               1,155 Americans.25 A 95% conﬁdence interval for the mean number of hours spent relaxing or pursuing
                  activities they enjoy was (1.38, 1.92).

                (a) Interpret this interval in context of the data.
                (b) Suppose another set of researchers reported a conﬁdence interval with a larger margin of error based on
                   the same sample of 1,155 Americans. How does their conﬁdence level compare to the conﬁdence level
                      of the interval stated above?
                 (c) Suppose next year a new survey asking the same question is conducted, and this time the sample size
                          is 2,500. Assuming that the population characteristics, with respect to how much time people spend
                    relaxing after work, have not changed much within a year. How will the margin of error of the 95%
                  conﬁdence interval constructed based on data from the new survey compare to the margin of error of
                   the interval stated above?

               5.28  Minimum wage, Part II. In Exercise 5.21, we learned that a Rasmussen Reports survey of 1,000 US
                adults found that 42% believe raising the minimum wage will help the economy. Construct a 99% conﬁdence
                 interval for the true proportion of US adults who believe this.

               5.29  Testing for food safety. A food safety inspector is called upon to investigate a restaurant with a few
              customer reports of poor sanitation practices. The food safety inspector uses a hypothesis testing framework
                to evaluate whether regulations are not being met. If he decides the restaurant is in gross violation, its license
                to serve food will be revoked.

                (a) Write the hypotheses in words.
                (b) What is a Type 1 Error in this context?
                 (c) What is a Type 2 Error in this context?
                (d) Which error is more problematic for the restaurant owner? Why?
                 (e) Which error is more problematic for the diners? Why?
                  (f) As a diner, would you prefer that the food safety inspector requires strong evidence or very strong
                   evidence of health concerns before revoking a restaurant’s license? Explain your reasoning.

               5.30  True or false. Determine if the following statements are true or false, and explain your reasoning. If
                   false, state how it could be corrected.

                (a)  If a given value (for example, the null hypothesized value of a parameter) is within a 95% conﬁdence
                      interval, it will also be within a 99% conﬁdence interval.
                (b) Decreasing the signiﬁcance level (α) will increase the probability of making a Type 1 Error.
                 (c) Suppose the null hypothesis is p = 0.5 and we fail to reject H0. Under this scenario, the true population
                   proportion is 0.5.
                (d) With large sample sizes, even small diﬀerences between the null value and the observed point estimate,
                  a diﬀerence often called the eﬀect size, will be identiﬁed as statistically signiﬁcant.

               5.31  Unemployment and relationship problems. A USA Today/Gallup poll asked a group of unemployed
             and underemployed Americans if they have had major problems in their relationships with their spouse or
               another close family member as a result of not having a job (if unemployed) or not having a full-time job (if
               underemployed). 27% of the 1,145 unemployed respondents and 25% of the 675 underemployed respondents
                said they had major problems in relationships as a result of their employment status.

                (a) What are the hypotheses for evaluating if the proportions of unemployed and underemployed people
               who had relationship problems were diﬀerent?
                (b) The p-value for this hypothesis test is approximately 0.35. Explain what this means in context of the
                   hypothesis test and the data.





                   25National Opinion Research Center, General Social Survey, 2018.

---

# OpenIntro Statistics, 4th edition

## 5.3 — Hypothesis testing for a proportion

### PDF page 205

5.3. HYPOTHESIS TESTING FOR A PROPORTION                                                205


5.32  Nearsighted. It is believed that nearsightedness aﬀects about 8% of all children. In a random sample
of 194 children, 21 are nearsighted. Conduct a hypothesis test for the following question: do these data
provide evidence that the 8% value is inaccurate?

5.33  Nutrition labels. The nutrition label on a bag of potato chips says that a one ounce (28 gram) serving
of potato chips has 130 calories and contains ten grams of fat, with three grams of saturated fat. A random
sample of 35 bags yielded a conﬁdence interval for the number of calories per bag of 128.2 to 139.8 calories.
Is there evidence that the nutrition label does not provide an accurate measure of calories in the bags of
potato chips?

5.34 CLT for proportions. Deﬁne the term “sampling distribution” of the sample proportion, and describe
how the shape, center, and spread of the sampling distribution change as the sample size increases when
p = 0.1.

5.35  Practical vs. statistical signiﬁcance. Determine whether the following statement is true or false,
and explain your reasoning: “With large sample sizes, even small diﬀerences between the null value and the
observed point estimate can be statistically signiﬁcant.”

5.36 Same observation, different sample size. Suppose you conduct a hypothesis test based on a sample
where the sample size is n = 50, and arrive at a p-value of 0.08. You then refer back to your notes and
discover that you made a careless mistake, the sample size should have been n = 500. Will your p-value
increase, decrease, or stay the same? Explain.

5.37  Gender pay gap in medicine. A study examined the average pay for men and women entering the
workforce as doctors for 21 diﬀerent positions.26

(a)  If each gender was equally paid, then we would expect about half of those positions to have men paid
   more than women and women would be paid more than men in the other half of positions.  Write
    appropriate hypotheses to test this scenario.
(b) Men were, on average, paid more in 19 of those 21 positions. Complete a hypothesis test using your
    hypotheses from part (a).





  26Lo Sasso AT et al. “The $16,819 Pay Gap For Newly Trained Physicians: The Unexplained Trend Of Men
Earning More Than Women”. In: Health Aﬀairs 30.2 (2011).

---

# OpenIntro Statistics, 4th edition

## 6.1 — Inference for a single proportion

### PDF page 206

206

Chapter 6

Inference for categorical data





6.1 Inference for a single proportion

6.2 Difference of two proportions

6.3 Testing for goodness of ﬁt using chi-square

6.4 Testing for independence in two-way tables

---

# OpenIntro Statistics, 4th edition

## 6.1 — Inference for a single proportion

### PDF page 207

207





In this chapter, we apply the methods and ideas from Chapter 5 in

several contexts for categorical data. We’ll start by revisiting what we

learned for a single proportion, where the normal distribution can be

used to model the uncertainty in the sample proportion. Next, we apply

these same ideas to analyze the diﬀerence of two proportions using the

normal model. Later in the chapter, we apply inference techniques to

contingency tables; while we will use a diﬀerent distribution in this

context, the core ideas of hypothesis testing remain the same.





For videos, slides, and other resources, please visit
www.openintro.org/os

---

# OpenIntro Statistics, 4th edition

## 6.1 — Inference for a single proportion

### PDF page 208

208                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA


        6.1  Inference for a single proportion



            We encountered inference methods for a single proportion in Chapter 5, exploring point esti-
              mates, conﬁdence intervals, and hypothesis tests. In this section, we’ll do a review of these topics and
                also how to choose an appropriate sample size when collecting data for single proportion contexts.


            6.1.1  Identifying when the sample proportion is nearly normal

            A sample proportion ˆp can be modeled using a normal distribution when the sample observations
               are independent and the sample size is suﬃciently large.


             SAMPLING DISTRIBUTION OF  ˆpˆpˆp
             The sampling distribution for ˆp based on a sample of size n from a population with a true
                proportion p is nearly normal when:

                      1. The sample’s observations are independent, e.g. are from a simple random sample.

                      2. We expected to see at least 10 successes and 10 failures in the sample, i.e. np ≥10 and
                    n(1 −p) ≥10. This is called the success-failure condition.

            When these conditions are met, then the sampling distribution of ˆp is nearly normal with mean
                    q p(1−p)
               p and standard error SE =      n     .


                   Typically we don’t know the true proportion p, so we substitute some value to check conditions
            and estimate the standard error. For conﬁdence intervals, the sample proportion ˆp is used to check
              the success-failure condition and compute the standard error. For hypothesis tests, typically the
                null value – that is, the proportion claimed in the null hypothesis – is used in place of p.


            6.1.2  Conﬁdence intervals for a proportion

            A conﬁdence interval provides a range of plausible values for the parameter p, and when ˆp can
             be modeled using a normal distribution, the conﬁdence interval for p takes the form

                                                                                       ˆp ± z⋆× SE



          EXAMPLE 6.1
         A simple random sample of 826 payday loan borrowers was surveyed to better understand their
                interests around regulation and costs. 70% of the responses supported new regulations on payday
                lenders. Is it reasonable to model ˆp = 0.70 using a normal distribution?

           The data are a random sample, so the observations are independent and representative of the
              population of interest.

         We also must check the success-failure condition, which we do using ˆp in place of p when computing
             a conﬁdence interval:

                      Support: np ≈826 × 0.70 = 578        Not: n(1 −p) ≈826 × (1 −0.70) = 248

              Since both values are at least 10, we can use the normal distribution to model ˆp.

---

# OpenIntro Statistics, 4th edition

## 6.1 — Inference for a single proportion

### PDF page 209

6.1. INFERENCE FOR A SINGLE PROPORTION                                                  209



GUIDED PRACTICE 6.2
Estimate the standard error of ˆp = 0.70. Because p is unknown and the standard error is for a
conﬁdence interval, use ˆp in place of p in the formula.1




EXAMPLE 6.3
Construct a 95% conﬁdence interval for p, the proportion of payday borrowers who support increased
regulation for payday lenders.

Using the point estimate 0.70, z⋆= 1.96 for a 95% conﬁdence interval, and the standard error
SE = 0.016 from Guided Practice 6.2, the conﬁdence interval is

        point estimate ± z⋆× SE →   0.70 ± 1.96 × 0.016 →   (0.669, 0.731)

We are 95% conﬁdent that the true proportion of payday borrowers who supported regulation at
the time of the poll was between 0.669 and 0.731.



  CONFIDENCE INTERVAL FOR A SINGLE PROPORTION
  Once you’ve determined a one-proportion conﬁdence interval would be helpful for an application,
  there are four steps to constructing the interval:

  Prepare. Identify ˆp and n, and determine what conﬁdence level you wish to use.

  Check. Verify the conditions to ensure  ˆp is nearly normal.  For one-proportion conﬁdence
         intervals, use ˆp in place of p to check the success-failure condition.

  Calculate.  If the conditions hold, compute SE using ˆp, ﬁnd z⋆, and construct the interval.

  Conclude. Interpret the conﬁdence interval in the context of the problem.


For additional one-proportion conﬁdence interval examples, see Section 5.2.


6.1.3  Hypothesis testing for a proportion

    One possible regulation for payday lenders is that they would be required to do a credit check
and evaluate debt payments against the borrower’s ﬁnances. We would like to know: would borrowers
support this form of regulation?


GUIDED PRACTICE 6.4
Set up hypotheses to evaluate whether borrowers have a majority support or majority opposition
for this type of regulation.2


    To apply the normal distribution framework in the context of a hypothesis test for a proportion,
the independence and success-failure conditions must be satisﬁed. In a hypothesis test, the successfailure condition is checked using the null proportion: we verify np0 and n(1 −p0) are at least 10,
where p0 is the null value.





   1SE = q p(1−p)n  ≈ q 0.70(1−0.70)826   = 0.016.
   2H0: p = 0.50. HA:  p̸ = 0.50.

---

# OpenIntro Statistics, 4th edition

## 6.1 — Inference for a single proportion

### PDF page 210

210                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA



           GUIDED PRACTICE 6.5
          Do payday loan borrowers support a regulation that would require lenders to pull their credit report
            and evaluate their debt payments? From a random sample of 826 borrowers, 51% said they would
             support such a regulation.  Is it reasonable to model ˆp = 0.51 using a normal distribution for a
              hypothesis test here?3




          EXAMPLE 6.6
             Using the hypotheses and data from Guided Practice 6.4 and 6.5, evaluate whether the poll provides
              convincing evidence that a majority of payday loan borrowers support a new regulation that would
               require lenders to pull credit reports and evaluate debt payments.

            With hypotheses already set up and conditions checked, we can move onto calculations. The standard
               error in the context of a one-proportion hypothesis test is computed using the null value, p0:

                     r p0(1 −p0) r 0.5(1 −0.5)
                          SE =        =         = 0.017
                                        n             826

         A picture of the normal model is shown below with the p-value represented by the shaded region.





                                           0.45   0.47   0.48   0.5   0.52   0.53   0.55


            Based on the normal model, the test statistic can be computed as the Z-score of the point estimate:

                                         point estimate −null value    0.51 −0.50
                        Z =                =       = 0.59
                                  SE                  0.017

           The single tail area is 0.2776, and the p-value, represented by both tail areas together, is 0.5552.
             Because the p-value is larger than 0.05, we do not reject H0. The poll does not provide convincing
              evidence that a majority of payday loan borrowers support or oppose regulations around credit
              checks and evaluation of debt payments.



             HYPOTHESIS TESTING FOR A SINGLE PROPORTION
              Once you’ve determined a one-proportion hypothesis test is the correct procedure, there are
                 four steps to completing the test:

              Prepare. Identify the parameter of interest, list hypotheses, identify the signiﬁcance level, and
                        identify ˆp and n.

             Check. Verify conditions to ensure ˆp is nearly normal under H0. For one-proportion hypothesis
                          tests, use the null value to check the success-failure condition.

               Calculate.  If the conditions hold, compute the standard error, again using p0, compute the
                        Z-score, and identify the p-value.

              Conclude. Evaluate the hypothesis test by comparing the p-value to α, and provide a conclu-
                       sion in the context of the problem.


             For additional one-proportion hypothesis test examples, see Section 5.3.


                   3Independence holds since the poll is based on a random sample. The success-failure condition also holds, which
                       is checked using the null value (p0 = 0.5) from H0: np0 = 826 × 0.5 = 413, n(1 −p0) = 826 × 0.5 = 413.

---

# OpenIntro Statistics, 4th edition

## 6.1 — Inference for a single proportion

### PDF page 211

6.1. INFERENCE FOR A SINGLE PROPORTION                                                  211


6.1.4 When one or more conditions aren’t met

    We’ve spent a lot of time discussing conditions for when ˆp can be reasonably modeled by a
normal distribution. What happens when the success-failure condition fails? What about when the
independence condition fails? In either case, the general ideas of conﬁdence intervals and hypothesis
tests remain the same, but the strategy or technique used to generate the interval or p-value change.
   When the success-failure condition isn’t met for a hypothesis test, we can simulate the null
distribution of ˆp using the null value, p0. The simulation concept is similar to the ideas used in the
malaria case study presented in Section 2.3, and an online section outlines this strategy:

                          www.openintro.org/r?go=stat sim prop ht

For a conﬁdence interval when the success-failure condition isn’t met, we can use what’s called the
Clopper-Pearson interval. The details are beyond the scope of this book. However, there are
many internet resources covering this topic.
    The independence condition is a more nuanced requirement. When it isn’t met, it is important
to understand how and why it isn’t met. For example, if we took a cluster sample (see Section 1.3),
suitable statistical methods are available but would be beyond the scope of even most second or
third courses in statistics. On the other hand, we’d be stretched to ﬁnd any method that we could
conﬁdently apply to correct the inherent biases of data from a convenience sample.
    While this book is scoped to well-constrained statistical problems, do remember that this is
just the ﬁrst book in what is a large library of statistical methods that are suitable for a very wide
range of data and contexts.

---

# OpenIntro Statistics, 4th edition

## 6.1 — Inference for a single proportion

### PDF page 212

212                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA


            6.1.5  Choosing a sample size when estimating a proportion

             When collecting data, we choose a sample size suitable for the purpose of the study. Often
              times this means choosing a sample size large enough that the margin of error – which is the
              part we add and subtract from the point estimate in a conﬁdence interval – is suﬃciently small that
              the sample is useful. For example, our task might be to ﬁnd a sample size n so that the sample
              proportion is within ±0.04 of the actual proportion in a 95% conﬁdence interval.


          EXAMPLE 6.7
         A university newspaper is conducting a survey to determine what fraction of students support a
             $200 per year increase in fees to pay for a new football stadium. How big of a sample is required to
              ensure the margin of error is smaller than 0.04 using a 95% conﬁdence level?

           The margin of error for a sample proportion is

                          r p(1 −p)
                                                       z⋆
                                                n

           Our goal is to ﬁnd the smallest sample size n so that this margin of error is smaller than 0.04. For
             a 95% conﬁdence level, the value z⋆corresponds to 1.96:

                         r p(1 −p)
                                                  1.96 ×       < 0.04
                                               n

             There are two unknowns in the equation: p and n. If we have an estimate of p, perhaps from a prior
               survey, we could enter in that value and solve for n. If we have no such estimate, we must use some
              other value for p. It turns out that the margin of error is largest when p is 0.5, so we typically use
                this worst case value if no estimate of the proportion is available:

                        r 0.5(1 −0.5)
                                                1.96 ×         < 0.04
                                              n
                                                           0.5(1 −0.5)
                                                  1.962 ×        < 0.042
                                              n
                                                           0.5(1 −0.5)
                                                  1.962 ×        < n
                                                              0.042
                                                            600.25 < n

         We would need over 600.25 participants, which means we need 601 participants or more, to ensure
              the sample proportion is within 0.04 of the true proportion with 95% conﬁdence.


             When an estimate of the proportion is available, we use it in place of the worst case proportion
               value, 0.5.

---

# OpenIntro Statistics, 4th edition

## 6.1 — Inference for a single proportion

### PDF page 213

6.1. INFERENCE FOR A SINGLE PROPORTION                                                  213



GUIDED PRACTICE 6.8
A manager is about to oversee the mass production of a new tire model in her factory, and she would
like to estimate what proportion of these tires will be rejected through quality control. The quality
control team has monitored the last three tire models produced by the factory, failing 1.7% of tires
in the ﬁrst model, 6.2% of the second model, and 1.3% of the third model. The manager would like
to examine enough tires to estimate the failure rate of the new tire model to within about 1% with
a 90% conﬁdence level. There are three diﬀerent failure rates to choose from. Perform the sample
size computation for each separately, and identify three sample sizes to consider.4




EXAMPLE 6.9
The sample sizes vary widely in Guided Practice 6.8. Which of the three would you suggest using?
What would inﬂuence your choice?

We could examine which of the old models is most like the new model, then choose the corresponding
sample size. Or if two of the previous estimates are based on small samples while the other is based
on a larger sample, we might consider the value corresponding to the larger sample. There are also
other reasonable approaches.

Also observe that the success-failure condition would need to be checked in the ﬁnal sample. For
instance, if we sampled n = 1584 tires and found a failure rate of 0.5%, the normal approximation
would not be reasonable, and we would require more advanced statistical methods for creating the
conﬁdence interval.



GUIDED PRACTICE 6.10
Suppose we want to continually track the support of payday borrowers for regulation on lenders,
where we would conduct a new poll every month. Running such frequent polls is expensive, so we
decide a wider margin of error of 5% for each individual survey would be acceptable. Based on
the original sample of borrowers where 70% supported some form of regulation, how big should our
monthly sample be for a margin of error of 0.05 with 95% conﬁdence?5





   4For a 90% conﬁdence interval, z⋆= 1.65, and since an estimate of the proportion 0.017 is available, we’ll use it
in the margin of error formula:

      r 0.017(1 −0.017)                     0.017(1 −0.017)       0.01  2
       1.65 ×            < 0.01  →             <       →     454.96 < n
                 n                          n              1.65

For sample size calculations, we always round up, so the ﬁrst tire model suggests 455 tires would be suﬃcient.
 A similar computation can be accomplished using 0.062 and 0.013 for p, and you should verify that using these
proportions results in minimum sample sizes of 1584 and 350 tires, respectively.
   5We complete the same computations as before, except now we use 0.70 instead of 0.5 for p:

            r p(1 −p)    r 0.70(1 −0.70)
                     1.96 ×         ≈1.96 ×              ≤0.05  →    n ≥322.7
                         n                n

A sample size of 323 or more would be reasonable. (Reminder: always round up for sample size calculations!) Given
that we plan to track this poll over time, we also may want to periodically repeat these calculations to ensure that
we’re being thoughtful in our sample size recommendations in case the baseline rate ﬂuctuates.

---

# OpenIntro Statistics, 4th edition

## 6.1 — Inference for a single proportion

### PDF page 214

214                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA


           Exercises


                6.1  Vegetarian college students. Suppose that 8% of college students are vegetarians. Determine if the
                following statements are true or false, and explain your reasoning.

                (a) The distribution of the sample proportions of vegetarians in random samples of size 60 is approximately
                 normal since n ≥30.
                (b) The distribution of the sample proportions of vegetarian college students in random samples of size 50
                          is right skewed.
                 (c) A random sample of 125 college students where 12% are vegetarians would be considered unusual.
                (d) A random sample of 250 college students where 12% are vegetarians would be considered unusual.
                 (e) The standard error would be reduced by one-half if we increased the sample size from 125 to 250.

                6.2  Young Americans, Part I. About 77% of young adults think they can achieve the American dream.
              Determine if the following statements are true or false, and explain your reasoning.6

                (a) The distribution of sample proportions of young Americans who think they can achieve the American
                dream in samples of size 20 is left skewed.
                (b) The distribution of sample proportions of young Americans who think they can achieve the American
                dream in random samples of size 40 is approximately normal since n ≥30.
                 (c) A random sample of 60 young Americans where 85% think they can achieve the American dream would
                 be considered unusual.
                (d) A random sample of 120 young Americans where 85% think they can achieve the American dream would
                 be considered unusual.

                6.3  Orange tabbies. Suppose that 90% of orange tabby cats are male. Determine if the following state-
              ments are true or false, and explain your reasoning.

                (a) The distribution of sample proportions of random samples of size 30 is left skewed.
                (b) Using a sample size that is 4 times as large will reduce the standard error of the sample proportion by
                     one-half.
                 (c) The distribution of sample proportions of random samples of size 140 is approximately normal.
                (d) The distribution of sample proportions of random samples of size 280 is approximately normal.

                6.4  Young Americans, Part II. About 25% of young Americans have delayed starting a family due to
               the continued economic slump. Determine if the following statements are true or false, and explain your
                reasoning.7

                (a) The distribution of sample proportions of young Americans who have delayed starting a family due to
                   the continued economic slump in random samples of size 12 is right skewed.
                (b) In order for the distribution of sample proportions of young Americans who have delayed starting a
                   family due to the continued economic slump to be approximately normal, we need random samples
                 where the sample size is at least 40.
                 (c) A random sample of 50 young Americans where 20% have delayed starting a family due to the continued
                  economic slump would be considered unusual.
                (d) A random sample of 150 young Americans where 20% have delayed starting a family due to the continued
                  economic slump would be considered unusual.
                 (e) Tripling the sample size will reduce the standard error of the sample proportion by one-third.





                  6A. Vaughn. “Poll ﬁnds young adults optimistic, but not about money”. In: Los Angeles Times (2011).
                   7Demos.org. “The State of Young America: The Poll”. In: (2011).

---

# OpenIntro Statistics, 4th edition

## 6.1 — Inference for a single proportion

### PDF page 215

6.1. INFERENCE FOR A SINGLE PROPORTION                                                  215


6.5  Gender equality. The General Social Survey asked a random sample of 1,390 Americans the following
question: “On the whole, do you think it should or should not be the government’s responsibility to promote
equality between men and women?” 82% of the respondents said it “should be”. At a 95% conﬁdence level,
this sample has 2% margin of error. Based on this information, determine if the following statements are
true or false, and explain your reasoning.8

(a) We are 95% conﬁdent that between 80% and 84% of Americans in this sample think it’s the government’s
     responsibility to promote equality between men and women.
(b) We are 95% conﬁdent that between 80% and 84% of all Americans think it’s the government’s respon-
     sibility to promote equality between men and women.
(c)  If we considered many random samples of 1,390 Americans, and we calculated 95% conﬁdence intervals
     for each, 95% of these intervals would include the true population proportion of Americans who think
      it’s the government’s responsibility to promote equality between men and women.
(d) In order to decrease the margin of error to 1%, we would need to quadruple (multiply by 4) the sample
     size.
(e) Based on this conﬁdence interval, there is suﬃcient evidence to conclude that a majority of Americans
    think it’s the government’s responsibility to promote equality between men and women.

6.6  Elderly drivers. The Marist Poll published a report stating that 66% of adults nationally think licensed
drivers should be required to retake their road test once they reach 65 years of age.  It was also reported
that interviews were conducted on 1,018 American adults, and that the margin of error was 3% using a 95%
conﬁdence level.9

(a) Verify the margin of error reported by The Marist Poll.
(b) Based on a 95% conﬁdence interval, does the poll provide convincing evidence that more than 70% of
    the population think that licensed drivers should be required to retake their road test once they turn
    65?

6.7  Fireworks on July 4th. A local news outlet reported that 56% of 600 randomly sampled Kansas
residents planned to set oﬀﬁreworks on July 4th. Determine the margin of error for the 56% point estimate
using a 95% conﬁdence level.10

6.8  Life rating in Greece. Greece has faced a severe economic crisis since the end of 2009. A Gallup poll
surveyed 1,000 randomly sampled Greeks in 2011 and found that 25% of them said they would rate their
lives poorly enough to be considered “suﬀering”.11

(a) Describe the population parameter of interest. What is the value of the point estimate of this parameter?
(b) Check if the conditions required for constructing a conﬁdence interval based on these data are met.
(c) Construct a 95% conﬁdence interval for the proportion of Greeks who are “suﬀering”.
(d) Without doing any calculations, describe what would happen to the conﬁdence interval if we decided to
    use a higher conﬁdence level.
(e) Without doing any calculations, describe what would happen to the conﬁdence interval if we used a
    larger sample.

6.9  Study abroad. A survey on 1,509 high school seniors who took the SAT and who completed an optional
web survey shows that 55% of high school seniors are fairly certain that they will participate in a study
abroad program in college.12

(a) Is this sample a representative sample from the population of all high school seniors in the US? Explain
    your reasoning.
(b) Let’s suppose the conditions for inference are met. Even if your answer to part (a) indicated that this
    approach would not be reliable, this analysis may still be interesting to carry out (though not report).
    Construct a 90% conﬁdence interval for the proportion of high school seniors (of those who took the
   SAT) who are fairly certain they will participate in a study abroad program in college, and interpret
     this interval in context.
(c) What does “90% conﬁdence” mean?
(d) Based on this interval, would it be appropriate to claim that the majority of high school seniors are
     fairly certain that they will participate in a study abroad program in college?

    8National Opinion Research Center, General Social Survey, 2018.
    9Marist Poll, Road Rules: Re-Testing Drivers at Age 65?, March 4, 2011.
   10Survey USA, News Poll #19333, data collected on June 27, 2012.
   11Gallup World, More Than One in 10 “Suﬀering” Worldwide, data collected throughout 2011.
  12studentPOLL, College-Bound Students’ Interests in Study Abroad and Other International Learning Activities,
January 2008.

---

# OpenIntro Statistics, 4th edition

## 6.1 — Inference for a single proportion

### PDF page 216

216                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA


               6.10  Legalization of marijuana, Part I. The General Social Survey asked 1,578 US residents: “Do you
               think the use of marijuana should be made legal, or not?” 61% of the respondents said it should be made
                  legal.13

                (a) Is 61% a sample statistic or a population parameter? Explain.
                (b) Construct a 95% conﬁdence interval for the proportion of US residents who think marijuana should be
               made legal, and interpret it in the context of the data.
                 (c) A critic points out that this 95% conﬁdence interval is only accurate if the statistic follows a normal
                     distribution, or if the normal model is a good approximation. Is this true for these data? Explain.
                (d) A news piece on this survey’s ﬁndings states, “Majority of Americans think marijuana should be legal-
                     ized.” Based on your conﬁdence interval, is this news piece’s statement justiﬁed?

               6.11  National Health Plan, Part I. A Kaiser Family Foundation poll for US adults in 2019 found that 79%
                 of Democrats, 55% of Independents, and 24% of Republicans supported a generic “National Health Plan”.
              There were 347 Democrats, 298 Republicans, and 617 Independents surveyed.14

                (a) A political pundit on TV claims that a majority of Independents support a National Health Plan. Do
                    these data provide strong evidence to support this type of statement?
                (b) Would you expect a conﬁdence interval for the proportion of Independents who oppose the public option
                   plan to include 0.5? Explain.

               6.12  Is college worth it? Part I. Among a simple random sample of 331 American adults who do not have
              a four-year college degree and are not currently enrolled in school, 48% said they decided not to go to college
               because they could not aﬀord school.15

                (a) A newspaper article states that only a minority of the Americans who decide not to go to college do
                    so because they cannot aﬀord it and uses the point estimate from this survey as evidence. Conduct a
                   hypothesis test to determine if these data provide strong evidence supporting this statement.
                (b) Would you expect a conﬁdence interval for the proportion of American adults who decide not to go to
                     college because they cannot aﬀord it to include 0.5? Explain.

               6.13  Taste test. Some people claim that they can tell the diﬀerence between a diet soda and a regular soda
                 in the ﬁrst sip. A researcher wanting to test this claim randomly sampled 80 such people. He then ﬁlled 80
                plain white cups with soda, half diet and half regular through random assignment, and asked each person
                to take one sip from their cup and identify the soda as diet or regular. 53 participants correctly identiﬁed
               the soda.

                (a) Do these data provide strong evidence that these people are any better or worse than random guessing
                    at telling the diﬀerence between diet and regular soda?
                (b) Interpret the p-value in this context.

               6.14  Is college worth it? Part II. Exercise 6.12 presents the results of a poll where 48% of 331 Americans
            who decide to not go to college do so because they cannot aﬀord it.

                (a) Calculate a 90% conﬁdence interval for the proportion of Americans who decide to not go to college
                  because they cannot aﬀord it, and interpret the interval in context.
                (b) Suppose we wanted the margin of error for the 90% conﬁdence level to be about 1.5%. How large of a
                   survey would you recommend?

               6.15  National Health Plan, Part II. Exercise 6.11 presents the results of a poll evaluating support for a
                generic “National Health Plan” in the US in 2019, reporting that 55% of Independents are supportive. If we
              wanted to estimate this number to within 1% with 90% conﬁdence, what would be an appropriate sample
                 size?

               6.16  Legalize Marijuana, Part II. As discussed in Exercise 6.10, the General Social Survey reported a
              sample where about 61% of US residents thought marijuana should be made legal. If we wanted to limit the
              margin of error of a 95% conﬁdence interval to 2%, about how many Americans would we need to survey?





                   13National Opinion Research Center, General Social Survey, 2018.
                   14Kaiser Family Foundation, The Public On Next Steps For The ACA And Proposals To Expand Coverage, data
                  collected between Jan 9-14, 2019.
                15Pew Research Center Publications, Is College Worth It?, data collected between March 15-29, 2011.

---

# OpenIntro Statistics, 4th edition

## 6.2 — Difference of two proportions

### PDF page 217

6.2. DIFFERENCE OF TWO PROPORTIONS                                                      217


6.2  Difference of two proportions



   We would like to extend the methods from Section 6.1 to apply conﬁdence intervals and hypothesis tests to diﬀerences in population proportions: p1 −p2. In our investigations, we’ll identify
a reasonable point estimate of p1 −p2 based on the sample, and you may have already guessed its
form:  ˆp1 −ˆp2. Next, we’ll apply the same processes we used in the single-proportion context: we
verify that the point estimate can be modeled using a normal distribution, we compute the estimate’s
standard error, and we apply our inferential framework.


6.2.1  Sampling distribution of the difference of two proportions

     Like with ˆp, the diﬀerence of two sample proportions ˆp1 −ˆp2 can be modeled using a normal
distribution when certain conditions are met. First, we require a broader independence condition,
and secondly, the success-failure condition must be met by both groups.


  CONDITIONS FOR THE SAMPLING DISTRIBUTION OF ˆp1ˆp1ˆp1 −ˆp2−ˆp2−ˆp2 TO BE NORMAL
  The diﬀerence ˆp1 −ˆp2 can be modeled using a normal distribution when

     • Independence, extended. The data are independent within and between the two groups.
       Generally this is satisﬁed if the data come from two independent random samples or if
        the data come from a randomized experiment.

     • Success-failure condition. The success-failure condition holds for both groups, where we
       check successes and failures in each group separately.

  When these conditions are satisﬁed, the standard error of ˆp1 −ˆp2 is

                s                                      p1(1 −p1)   p2(1 −p2)
                   SE =        +
                                      n1          n2

  where p1 and p2 represent the population proportions, and n1 and n2 represent the sample sizes.



6.2.2  Conﬁdence intervals for p1p1p1 −p2−p2−p2

We can apply the generic conﬁdence interval formula for a diﬀerence of two proportions, where we
use ˆp1 −ˆp2 as the point estimate and substitute the SE formula:

                             s                                                                 p1(1 −p1)   p2(1 −p2)
      point estimate ± z⋆× SE   →          ˆp1 −ˆp2 ± z⋆×        +
                                                                n1          n2

We can also follow the same Prepare, Check, Calculate, Conclude steps for computing a conﬁdence
interval or completing a hypothesis test. The details change a little, but the general approach remain
the same. Think about these steps when you apply statistical methods.

---

# OpenIntro Statistics, 4th edition

## 6.2 — Difference of two proportions

### PDF page 218

218                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA



          EXAMPLE 6.11
         We consider an experiment for patients who underwent cardiopulmonary resuscitation (CPR) for a
              heart attack and were subsequently admitted to a hospital. These patients were randomly divided
               into a treatment group where they received a blood thinner or the control group where they did not
               receive a blood thinner. The outcome variable of interest was whether the patients survived for at
                least 24 hours. The results are shown in Figure 6.1. Check whether we can model the diﬀerence in
             sample proportions using the normal distribution.

         We ﬁrst check for independence: since this is a randomized experiment, this condition is satisﬁed.

              Next, we check the success-failure condition for each group. We have at least 10 successes and 10
                 failures in each experiment arm (11, 14, 39, 26), so this condition is also satisﬁed.

            With both conditions satisﬁed, the diﬀerence in sample proportions can be reasonably modeled using
             a normal distribution for these data.



                                                      Survived  Died     Total
                                        Control          11      39       50
                                     Treatment        14      26       40
                                         Total            25      65       90

                      Figure 6.1: Results for the CPR study. Patients in the treatment group were given
                     a blood thinner, and patients in the control group were not.



          EXAMPLE 6.12
             Create and interpret a 90% conﬁdence interval of the diﬀerence for the survival rates in the CPR
               study.

               We’ll use pt for the survival rate in the treatment group and pc for the control group:

                                                14 −11 = 0.35 −0.22 = 0.13                                                                         ˆpt −ˆpc =
                                                40   50

         We use the standard error formula provided on page 217. As with the one-sample proportion case,
           we use the sample estimates of each proportion in the formula in the conﬁdence interval context:

                    r 0.35(1 −0.35)   0.22(1 −0.22)
                         SE ≈          +         = 0.095
                                                40             50

             For a 90% conﬁdence interval, we use z⋆= 1.65:

                        point estimate ± z⋆× SE →   0.13 ± 1.65 × 0.095 →   (−0.027, 0.287)

         We are 90% conﬁdent that blood thinners have a diﬀerence of -2.7% to +28.7% percentage point
             impact on survival rate for patients who are like those in the study. Because 0% is contained in
              the interval, we do not have enough information to say whether blood thinners help or harm heart
              attack patients who have been admitted after they have undergone CPR.

---

# OpenIntro Statistics, 4th edition

## 6.2 — Difference of two proportions

### PDF page 219

6.2. DIFFERENCE OF TWO PROPORTIONS                                                      219



GUIDED PRACTICE 6.13
A 5-year experiment was conducted to evaluate the eﬀectiveness of ﬁsh oils on reducing cardiovascular
events, where each subject was randomized into one of two treatment groups. We’ll consider heart
attack outcomes in these patients:

                                     heart attack  no event   Total
                         ﬁsh oil       145       12788    12933
                          placebo      200       12738    12938

Create a 95% conﬁdence interval for the eﬀect of ﬁsh oils on heart attacks for patients who are
well-represented by those in the study. Also interpret the interval in the context of the study.16




6.2.3  Hypothesis tests for the difference of two proportions

   A mammogram is an X-ray procedure used to check for breast cancer. Whether mammograms
should be used is part of a controversial discussion, and it’s the topic of our next example where we
learn about 2-proportion hypothesis tests when H0 is p1 −p2 = 0 (or equivalently, p1 = p2).
   A 30-year study was conducted with nearly 90,000 female participants. During a 5-year screening period, each woman was randomized to one of two groups: in the ﬁrst group, women received
regular mammograms to screen for breast cancer, and in the second group, women received regular
non-mammogram breast cancer exams. No intervention was made during the following 25 years of
the study, and we’ll consider death resulting from breast cancer over the full 30-year period. Results
from the study are summarized in Figure 6.2.
       If mammograms are much more eﬀective than non-mammogram breast cancer exams, then we
would expect to see additional deaths from breast cancer in the control group. On the other hand, if
mammograms are not as eﬀective as regular breast cancer exams, we would expect to see an increase
in breast cancer deaths in the mammogram group.

                                     Death from breast cancer?
                                           Yes      No
                   Mammogram       500       44,425
                               Control       505       44,405

                      Figure 6.2: Summary results for breast cancer study.



GUIDED PRACTICE 6.14
Is this study an experiment or an observational study?17





   16 Because the patients were randomized, the subjects are independent, both within and between the two groups.
The success-failure condition is also met for both groups as all counts are at least 10. This satisﬁes the conditions
necessary to model the diﬀerence in proportions using a normal distribution.
  Compute the sample proportions (ˆpﬁsh oil = 0.0112, ˆpplacebo = 0.0155), point estimate of the diﬀerence (0.0112 −
                    q 0.0112×0.9888    0.0155×0.9845
0.0155 = −0.0043), and standard error (SE =       12933   +     12938   = 0.00145). Next, plug the values into
the general formula for a conﬁdence interval, where we’ll use a 95% conﬁdence level with z⋆= 1.96:

                            −0.0043 ± 1.96 × 0.00145 →   (−0.0071, −0.0015)

We are 95% conﬁdent that ﬁsh oils decreases heart attacks by 0.15 to 0.71 percentage points (oﬀof a baseline of about
1.55%) over a 5-year period for subjects who are similar to those in the study. Because the interval is entirely below 0,
the data provide strong evidence that ﬁsh oil supplements reduce heart attacks in patients like those in the study.
   17This is an experiment. Patients were randomized to receive mammograms or a standard breast cancer exam. We
will be able to make causal conclusions based on this study.

---

# OpenIntro Statistics, 4th edition

## 6.2 — Difference of two proportions

### PDF page 220

220                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA



           GUIDED PRACTICE 6.15
              Set up hypotheses to test whether there was a diﬀerence in breast cancer deaths in the mammogram
            and control groups.18


                   In Example 6.16, we will check the conditions for using a normal distribution to analyze the
                results of the study. The details are very similar to that of conﬁdence intervals. However, when the
                null hypothesis is that p1 −p2 = 0, we use a special proportion called the pooled proportion to
              check the success-failure condition:

                    # of patients who died from breast cancer in the entire study
                                      ˆppooled =
                            # of patients in the entire study
                                         500 + 505
                    =
                                 500 + 44,425 + 505 + 44,405
                    = 0.0112

             This proportion is an estimate of the breast cancer death rate across the entire study, and it’s our
              best estimate of the proportions pmgm and pctrl  if the null hypothesis is true that pmgm = pctrl.
         We will also use this pooled proportion when computing the standard error.


          EXAMPLE 6.16
                 Is it reasonable to model the diﬀerence in proportions using a normal distribution in this study?

             Because the patients are randomized, they can be treated as independent, both within and between
              groups. We also must check the success-failure condition for each group. Under the null hypothesis,
              the proportions pmgm and pctrl are equal, so we check the success-failure condition with our best
              estimate of these values under H0, the pooled proportion from the two samples, ˆppooled = 0.0112:

                        ˆppooled × nmgm = 0.0112 × 44,925 = 503    (1 −ˆppooled) × nmgm = 0.9888 × 44,925 = 44,422
                          ˆppooled × nctrl = 0.0112 × 44,910 = 503     (1 −ˆppooled) × nctrl = 0.9888 × 44,910 = 44,407

           The success-failure condition is satisﬁed since all values are at least 10.  With both conditions
               satisﬁed, we can safely model the diﬀerence in proportions using a normal distribution.


            USE THE POOLED PROPORTION WHEN H0H0H0 IS p1p1p1 −p2−p2−p2 === 000
            When the null hypothesis is that the proportions are equal, use the pooled proportion (ˆppooled)
                 to verify the success-failure condition and estimate the standard error:

                                      number of “successes”    ˆp1n1 + ˆp2n2
                                                  ˆppooled =             =
                                        number of cases        n1 + n2

               Here ˆp1n1 represents the number of successes in sample 1 since

                                       number of successes in sample 1
                                                               ˆp1 =
                                                        n1

                  Similarly, ˆp2n2 represents the number of successes in sample 2.


                   In Example 6.16, the pooled proportion was used to check the success-failure condition.19 In the
              next example, we see the second place where the pooled proportion comes into play: the standard
               error calculation.



                  18H0: the breast cancer death rate for patients screened using mammograms is the same as the breast cancer death
                  rate for patients in the control, pmgm −pctrl = 0.
             HA: the breast cancer death rate for patients screened using mammograms is diﬀerent than the breast cancer death
                  rate for patients in the control, pmgm −pctrl̸ = 0.
                   19For an example of a two-proportion hypothesis test that does not require the success-failure condition to be met,
                  see Section 2.3.

---

# OpenIntro Statistics, 4th edition

## 6.2 — Difference of two proportions

### PDF page 221

6.2. DIFFERENCE OF TWO PROPORTIONS                                                      221



EXAMPLE 6.17
Compute the point estimate of the diﬀerence in breast cancer death rates in the two groups, and
use the pooled proportion ˆppooled = 0.0112 to calculate the standard error.

The point estimate of the diﬀerence in breast cancer death rates is

                                          500           505
                         ˆpmgm −ˆpctrl =        −
                                     500 + 44, 425   505 + 44, 405
                       = 0.01113 −0.01125
                       = −0.00012

The breast cancer death rate in the mammogram group was 0.012% less than in the control group.
Next, the standard error is calculated using the pooled proportion, ˆppooled:

           s                                   ˆppooled(1 −ˆppooled)    ˆppooled(1 −ˆppooled)
            SE =            +           = 0.00070
                         nmgm                   nctrl




EXAMPLE 6.18
Using the point estimate ˆpmgm −ˆpctrl = −0.00012 and standard error SE = 0.00070, calculate a
p-value for the hypothesis test and write a conclusion.

Just like in past tests, we ﬁrst compute a test statistic and draw a picture:

                         point estimate −null value   −0.00012 −0
             Z =                =        = −0.17
                       SE                 0.00070





                                      −0.0014          0           0.0014


The lower tail area is 0.4325, which we double to get the p-value: 0.8650. Because this p-value is
larger than 0.05, we do not reject the null hypothesis. That is, the diﬀerence in breast cancer death
rates is reasonably explained by chance, and we do not observe beneﬁts or harm from mammograms
relative to a regular breast exam.


    Can we conclude that mammograms have no beneﬁts or harm? Here are a few considerations
to keep in mind when reviewing the mammogram study as well as any other medical study:

   • We do not accept the null hypothesis, which means we don’t have suﬃcient evidence to conclude
     that mammograms reduce or increase breast cancer deaths.

   • If mammograms are helpful or harmful, the data suggest the eﬀect isn’t very large.

   • Are mammograms more or less expensive than a non-mammogram breast exam? If one option
       is much more expensive than the other and doesn’t oﬀer clear beneﬁts, then we should lean
     towards the less expensive option.

   • The study’s authors also found that mammograms led to overdiagnosis of breast cancer, which
     means some breast cancers were found (or thought to be found) but that these cancers would
     not cause symptoms during patients’ lifetimes. That is, something else would kill the patient
      before breast cancer symptoms appeared. This means some patients may have been treated for
      breast cancer unnecessarily, and this treatment is another cost to consider. It is also important
      to recognize that overdiagnosis can cause unnecessary physical or emotional harm to patients.

These considerations highlight the complexity around medical care and treatment recommendations.
Experts and medical boards who study medical treatments use considerations like those above to
provide their best recommendation based on the current evidence.

---

# OpenIntro Statistics, 4th edition

## 6.2 — Difference of two proportions

### PDF page 222

222                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA


            6.2.4  More on 2-proportion hypothesis tests (special topic)

             When we conduct a 2-proportion hypothesis test, usually H0 is p1 −p2 = 0. However, there
               are rare situations where we want to check for some diﬀerence in p1 and p2 that is some value other
             than 0. For example, maybe we care about checking a null hypothesis where p1 −p2 = 0.1.  In
              contexts like these, we generally use ˆp1 and ˆp2 to check the success-failure condition and construct
              the standard error.


           GUIDED PRACTICE 6.19
         A quadcopter company is considering a new manufacturer for rotor blades. The new manufacturer
             would be more expensive, but they claim their higher-quality blades are more reliable, with 3% more
              blades passing inspection than their competitor. Set up appropriate hypotheses for the test.20





                                  Figure 6.3: A Phantom quadcopter.
                 —————————–
                                    Photo by David J (http://ﬂic.kr/p/oiWLNu). CC-BY 2.0 license.
                                       This photo has been cropped and a border has been added.





                  20H0: The higher-quality blades will pass inspection 3% more frequently than the standard-quality blades. phighQ−
                 pstandard = 0.03. HA: The higher-quality blades will pass inspection some amount diﬀerent than 3% more often than
                 the standard-quality blades. phighQ −pstandard̸ = 0.03.

---

# OpenIntro Statistics, 4th edition

## 6.2 — Difference of two proportions

### PDF page 223

6.2. DIFFERENCE OF TWO PROPORTIONS                                                      223



EXAMPLE 6.20
The quality control engineer from Guided Practice 6.19 collects a sample of blades, examining 1000
blades from each company, and she ﬁnds that 899 blades pass inspection from the current supplier
and 958 pass inspection from the prospective supplier. Using these data, evaluate the hypotheses
from Guided Practice 6.19 with a signiﬁcance level of 5%.

First, we check the conditions. The sample is not necessarily random, so to proceed we must assume
the blades are all independent; for this sample we will suppose this assumption is reasonable, but
the engineer would be more knowledgeable as to whether this assumption is appropriate.  The
success-failure condition also holds for each sample.  Thus, the diﬀerence in sample proportions,
0.958 −0.899 = 0.059, can be said to come from a nearly normal distribution.

The standard error is computed using the two sample proportions since we do not use a pooled
proportion for this context:

             r 0.958(1 −0.958)   0.899(1 −0.899)
              SE =           +          = 0.0114
                                 1000             1000

In this hypothesis test, because the null is that p1 −p2 = 0.03, the sample proportions were used
for the standard error calculation rather than a pooled proportion.

Next, we compute the test statistic and use it to ﬁnd the p-value, which is depicted in Figure 6.4.

                          point estimate −null value   0.059 −0.03
              Z =                =        = 2.54
                        SE                 0.0114

Using a standard normal distribution for this test statistic, we identify the right tail area as 0.006,
and we double it to get the p-value:  0.012. We reject the null hypothesis because 0.012 is less
than 0.05.  Since we observed a larger-than-3% increase in blades that pass inspection, we have
statistically signiﬁcant evidence that the higher-quality blades pass inspection more than 3% as
often as the currently used blades, exceeding the company’s claims.




                                                            0.006



                                           0.03        0.059
                                                                          (null value)

        Figure 6.4: Distribution of the test statistic if the null hypothesis was true. The
        p-value is represented by the shaded areas.

---

# OpenIntro Statistics, 4th edition

## 6.2 — Difference of two proportions

### PDF page 224

224                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA


            6.2.5  Examining the standard error formula (special topic)

                  This subsection covers more theoretical topics that oﬀer deeper insights into the origins of the
              standard error formula for the diﬀerence of two proportions. Ultimately, all of the standard error
              formulas we encounter in this chapter and in Chapter 7 can be derived from the probability principles
                of Section 3.4.
               The formula for the standard error of the diﬀerence in two proportions can be deconstructed
               into the formulas for the standard errors of the individual sample proportions.  Recall that the
              standard error of the individual sample proportions ˆp1 and ˆp2 are

                  s                 s                                          p1(1 −p1)                             p2(1 −p2)
                                  SEˆp1 =                                 SEˆp2 =
                                          n1                                 n2

           The standard error of the diﬀerence of two sample proportions can be deconstructed from the
              standard errors of the separate sample proportions:

                             s
                     q                  p1(1 −p1)   p2(1 −p2)
                                        SEˆp1−ˆp2 =  SE2ˆp1 + SE2ˆp2 =        +                                                                n1          n2

             This special relationship follows from probability theory.


           GUIDED PRACTICE 6.21
               Prerequisite: Section 3.4. We can rewrite the equation above in a diﬀerent way:

                                     SE2ˆp1−ˆp2 = SE2ˆp1 + SE2ˆp2

             Explain where this formula comes from using the formula for the variability of the sum of two random
                variables.21





                 21The standard error squared represents the variance of the estimate. If X and Y are two random variables with
                 variances σ2x and σ2y, then the variance of X −Y  is σ2x + σ2y.  Likewise, the variance corresponding to ˆp1 −ˆp2 is
               σ2                             ˆp1            + σ2ˆp2. Because σ2ˆp1 and σ2ˆp2 are just another way of writing SE2ˆp1 and SE2ˆp2, the variance associated with ˆp1 −ˆp2
             may be written as SE2 + SE2                                                             ˆp1         ˆp2.

---

# OpenIntro Statistics, 4th edition

## 6.2 — Difference of two proportions

### PDF page 225

6.2. DIFFERENCE OF TWO PROPORTIONS                                                      225


Exercises


6.17  Social experiment, Part  I. A “social experiment” conducted by a TV program questioned what
people do when they see a very obviously bruised woman getting picked on by her boyfriend. On two
diﬀerent occasions at the same restaurant, the same couple was depicted. In one scenario the woman was
dressed “provocatively” and in the other scenario the woman was dressed “conservatively”. The table below
shows how many restaurant diners were present under each scenario, and whether or not they intervened.

                                                    Scenario
                                           Provocative   Conservative   Total
                                 Yes         5            15        20
                        Intervene
                           No         15           10        25
                                    Total       20           25        45

Explain why the sampling distribution of the diﬀerence between the proportions of interventions under
provocative and conservative scenarios does not follow an approximately normal distribution.

6.18  Heart transplant success. The Stanford University Heart Transplant Study was conducted to determine whether an experimental heart transplant program increased lifespan. Each patient entering the
program was oﬃcially designated a heart transplant candidate, meaning that he was gravely ill and might
beneﬁt from a new heart. Patients were randomly assigned into treatment and control groups. Patients in
the treatment group received a transplant, and those in the control group did not. The table below displays
how many patients survived and died in each group.22
                                                control   treatment
                                            alive     4        24
                                  dead     30        45

Suppose we are interested in estimating the diﬀerence in survival rate between the control and treatment
groups using a conﬁdence interval.  Explain why we cannot construct such an interval using the normal
approximation. What might go wrong if we constructed the conﬁdence interval despite this problem?

6.19  Gender and color preference. A study asked 1,924 male and 3,666 female undergraduate college
students their favorite color. A 95% conﬁdence interval for the diﬀerence between the proportions of males
and females whose favorite color is black (pmale −pfemale) was calculated to be (0.02, 0.06). Based on this
information, determine if the following statements are true or false, and explain your reasoning for each
statement you identify as false.23

(a) We are 95% conﬁdent that the true proportion of males whose favorite color is black is 2% lower to 6%
    higher than the true proportion of females whose favorite color is black.
(b) We are 95% conﬁdent that the true proportion of males whose favorite color is black is 2% to 6% higher
    than the true proportion of females whose favorite color is black.
(c) 95% of random samples will produce 95% conﬁdence intervals that include the true diﬀerence between
    the population proportions of males and females whose favorite color is black.
(d) We can conclude that there is a signiﬁcant diﬀerence between the proportions of males and females
    whose favorite color is black and that the diﬀerence between the two sample proportions is too large to
    plausibly be due to chance.
(e) The 95% conﬁdence interval for (pfemale −pmale) cannot be calculated with only the information given
    in this exercise.





   22B. Turnbull et al. “Survivorship of Heart Transplant Data”. In: Journal of the American Statistical Association
69 (1974), pp. 74–80.
  23L Ellis and C Ficek.  “Color preferences according to gender and sexual orientation”.  In:  Personality and
Individual Diﬀerences 31.8 (2001), pp. 1375–1379.

---

# OpenIntro Statistics, 4th edition

## 6.2 — Difference of two proportions

### PDF page 226

226                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA


               6.20  Government shutdown. The United States federal government shutdown of 2018–2019 occurred
              from December 22, 2018 until January 25, 2019, a span of 35 days. A Survey USA poll of 614 randomly
              sampled Americans during this time period reported that 48% of those who make less than $40,000 per
               year and 55% of those who make $40,000 or more per year said the government shutdown has not at all
               aﬀected them personally. A 95% conﬁdence interval for (p<40K −p≥40K), where p is the proportion of those
            who said the government shutdown has not at all aﬀected them personally, is (-0.16, 0.02). Based on this
                information, determine if the following statements are true or false, and explain your reasoning if you identify
               the statement as false.24

                (a) At the 5% signiﬁcance level, the data provide convincing evidence of a real diﬀerence in the proportion
               who are not aﬀected personally between Americans who make less than $40,000 annually and Americans
               who make $40,000 annually.
                (b) We are 95% conﬁdent that 16% more to 2% fewer Americans who make less than $40,000 per year are
                  not at all personally aﬀected by the government shutdown compared to those who make $40,000 or more
                   per year.
                 (c) A 90% conﬁdence interval for (p<40K −p≥40K) would be wider than the (−0.16, 0.02) interval.
                (d) A 95% conﬁdence interval for (p≥40K −p<40K) is (-0.02, 0.16).

               6.21  National Health Plan, Part III. Exercise 6.11 presents the results of a poll evaluating support for a
                 generically branded “National Health Plan” in the United States. 79% of 347 Democrats and 55% of 617
               Independents support a National Health Plan.

                (a) Calculate a 95% conﬁdence interval for the diﬀerence between the proportion of Democrats and Inde-
                  pendents who support a National Health Plan (pD −pI), and interpret it in this context. We have
                   already checked conditions for you.
                (b) True or false: If we had picked a random Democrat and a random Independent at the time of this poll,
                           it is more likely that the Democrat would support the National Health Plan than the Independent.

               6.22  Sleep deprivation, CA vs. OR, Part I. According to a report on sleep deprivation by the Centers for
               Disease Control and Prevention, the proportion of California residents who reported insuﬃcient rest or sleep
               during each of the preceding 30 days is 8.0%, while this proportion is 8.8% for Oregon residents. These
              data are based on simple random samples of 11,545 California and 4,691 Oregon residents. Calculate a 95%
              conﬁdence interval for the diﬀerence between the proportions of Californians and Oregonians who are sleep
               deprived and interpret it in context of the data.25

               6.23  Offshore drilling, Part I. A survey asked 827 randomly sampled registered voters in California “Do
              you support? Or do you oppose?  Drilling for oil and natural gas oﬀthe Coast of California? Or do you
               not know enough to say?” Below is the distribution of responses, separated based on whether or not the
               respondent graduated from college.26


                (a) What percent of college graduates and what percent of the
                    non-college graduates in this sample do not know enough to                       College Grad
                  have an opinion on drilling for oil and natural gas oﬀthe                    Yes   No
                  Coast of California?                                         Support       154    132
                (b) Conduct a hypothesis test to determine if the data provide      Oppose       180    126
                   strong evidence that the proportion of college graduates who     Do not know   104    131
                 do not have an opinion on this issue is diﬀerent than that of       Total         438    389
                    non-college graduates.


               6.24  Sleep deprivation, CA vs. OR, Part II. Exercise 6.22 provides data on sleep deprivation rates of
                Californians and Oregonians. The proportion of California residents who reported insuﬃcient rest or sleep
               during each of the preceding 30 days is 8.0%, while this proportion is 8.8% for Oregon residents. These data
                are based on simple random samples of 11,545 California and 4,691 Oregon residents.

                (a) Conduct a hypothesis test to determine if these data provide strong evidence the rate of sleep deprivation
                          is diﬀerent for the two states. (Reminder: Check conditions)
                (b) It is possible the conclusion of the test in part (a) is incorrect. If this is the case, what type of error was
                made?




                  24Survey USA, News Poll #24568, data collected on April 21, 2019.
                25CDC, Perceived Insuﬃcient Rest or Sleep Among Adults — United States, 2008.
                  26Survey USA, Election Poll #16804, data collected July 8-11, 2010.

---

# OpenIntro Statistics, 4th edition

## 6.2 — Difference of two proportions

### PDF page 227

6.2. DIFFERENCE OF TWO PROPORTIONS                                                      227


6.25  Offshore drilling, Part II. Results of a poll evaluating support for drilling for oil and natural gas oﬀ
the coast of California were introduced in Exercise 6.23.

                                                      College Grad
                                                Yes   No
                                  Support       154    132
                                Oppose       180    126
                           Do not know   104    131
                                     Total         438    389

(a) What percent of college graduates and what percent of the non-college graduates in this sample support
     drilling for oil and natural gas oﬀthe Coast of California?
(b) Conduct a hypothesis test to determine if the data provide strong evidence that the proportion of college
    graduates who support oﬀ-shore drilling in California is diﬀerent than that of non-college graduates.

6.26  Full body scan, Part I. A news article reports that “Americans have diﬀering views on two potentially
inconvenient and invasive practices that airports could implement to uncover potential terrorist attacks.”
This news piece was based on a survey conducted among a random sample of 1,137 adults nationwide, where
one of the questions on the survey was “Some airports are now using ‘full-body’ digital x-ray machines to
electronically screen passengers in airport security lines. Do you think these new x-ray machines should or
should not be used at airports?” Below is a summary of responses based on party aﬃliation.27

                                                          Party Aﬃliation
                                               Republican  Democrat   Independent
                       Should                    264         299         351
             Answer   Should not                 38          55          77
                       Don’t know/No answer      16          15          22
                         Total                      318         369         450

(a) Conduct an appropriate hypothesis test evaluating whether there is a diﬀerence in the proportion of
    Republicans and Democrats who think the full- body scans should be applied in airports. Assume that
     all relevant conditions are met.
(b) The conclusion of the test in part (a) may be incorrect, meaning a testing error was made. If an error
    was made, was it a Type 1 or a Type 2 Error? Explain.

6.27  Sleep deprived transportation workers. The National Sleep Foundation conducted a survey on
the sleep habits of randomly sampled transportation workers and a control sample of non-transportation
workers. The results of the survey are shown below.28
                                                        Transportation Professionals
                                                   Truck      Train    Bus/Taxi/Limo
                                     Control   Pilots   Drivers   Operators       Drivers
          Less than 6 hours of sleep     35      19      35        29            21
         6 to 8 hours of sleep         193     132     117       119           131
        More than 8 hours           64      51      51        32            58
          Total                       292     202     203       180           210

Conduct a hypothesis test to evaluate if these data provide evidence of a diﬀerence between the proportions
of truck drivers and non-transportation workers (the control group) who get less than 6 hours of sleep per
day, i.e. are considered sleep deprived.





   27S. Condon. “Poll: 4 in 5 Support Full-Body Airport Scanners”. In: CBS News (2010).
   28National Sleep Foundation, 2012 Sleep in America Poll: Transportation Workers’ Sleep, 2012.

---

# OpenIntro Statistics, 4th edition

## 6.2 — Difference of two proportions

### PDF page 228

228                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA


               6.28  Prenatal vitamins and Autism.  Researchers studying the link between prenatal vitamin use and
              autism surveyed the mothers of a random sample of children aged 24 - 60 months with autism and conducted
               another separate random sample for children with typical development. The table below shows the number of
              mothers in each group who did and did not use prenatal vitamins during the three months before pregnancy
                (periconceptional period).29

                                                                  Autism
                                                       Autism   Typical development   Total
                                Periconceptional  No vitamin    111            70           181
                                 prenatal vitamin   Vitamin       143            159           302
                                                  Total          254            229           483
                (a) State appropriate hypotheses to test for independence of use of prenatal vitamins during the three
                 months before pregnancy and autism.
                (b) Complete the hypothesis test and state an appropriate conclusion. (Reminder: Verify any necessary
                    conditions for the test.)
                 (c) A New York Times article reporting on this study was titled “Prenatal Vitamins May Ward OﬀAutism”.
              Do you ﬁnd the title of this article to be appropriate? Explain your answer. Additionally, propose an
                     alternative title.30

               6.29  HIV in sub-Saharan Africa. In July 2008 the US National Institutes of Health announced that it was
               stopping a clinical study early because of unexpected results. The study population consisted of HIV-infected
            women in sub-Saharan Africa who had been given single dose Nevaripine (a treatment for HIV) while giving
                 birth, to prevent transmission of HIV to the infant. The study was a randomized comparison of continued
               treatment of a woman (after successful childbirth) with Nevaripine vs Lopinavir, a second drug used to treat
             HIV. 240 women participated in the study; 120 were randomized to each of the two treatments. Twenty-
                four weeks after starting the study treatment, each woman was tested to determine if the HIV infection was
              becoming worse (an outcome called virologic failure). Twenty-six of the 120 women treated with Nevaripine
               experienced virologic failure, while 10 of the 120 women treated with the other drug experienced virologic
                  failure.31

                (a) Create a two-way table presenting the results of this study.
                (b) State appropriate hypotheses to test for diﬀerence in virologic failure rates between treatment groups.
                 (c) Complete the hypothesis test and state an appropriate conclusion. (Reminder: Verify any necessary
                    conditions for the test.)

               6.30  An apple a day keeps the doctor away. A physical education teacher at a high school wanting to
                increase awareness on issues of nutrition and health asked her students at the beginning of the semester
              whether they believed the expression “an apple a day keeps the doctor away”, and 40% of the students
              responded yes. Throughout the semester she started each class with a brief discussion of a study highlighting
                 positive eﬀects of eating more fruits and vegetables. She conducted the same apple-a-day survey at the end
                 of the semester, and this time 60% of the students responded yes. Can she used a two-proportion method
              from this section for this analysis? Explain your reasoning.





                   29R.J. Schmidt et al. “Prenatal vitamins, one-carbon metabolism gene variants, and risk for autism”. In: Epidemi-
                 ology 22.4 (2011), p. 476.
                  30R.C. Rabin. “Patterns: Prenatal Vitamins May Ward OﬀAutism”. In: New York Times (2011).
                    31S. Lockman et al. “Response to antiretroviral therapy after a single, peripartum dose of nevirapine”. In: Obstet-
                    rical & gynecological survey 62.6 (2007), p. 361.

---

# OpenIntro Statistics, 4th edition

## 6.3 — Testing for goodness of fit using chi-square

### PDF page 229

6.3. TESTING FOR GOODNESS OF FIT USING CHI-SQUARE                                      229


6.3  Testing for goodness of ﬁt using chi-square



     In this section, we develop a method for assessing a null model when the data are binned. This
technique is commonly used in two circumstances:

   • Given a sample of cases that can be classiﬁed into several groups, determine if the sample is
      representative of the general population.

   • Evaluate whether data resemble a particular distribution, such as a normal distribution or a
     geometric distribution.

Each of these scenarios can be addressed using the same statistical test: a chi-square test.
     In the ﬁrst case, we consider data from a random sample of 275 jurors in a small county. Jurors
identiﬁed their racial group, as shown in Figure 6.5, and we would like to determine if these jurors
are racially representative of the population.  If the jury is representative of the population, then
the proportions in the sample should roughly reﬂect the population of eligible jurors, i.e. registered
voters.

         Race                     White  Black   Hispanic  Other      Total
          Representation in juries       205     26       25       19       275
           Registered voters              0.72    0.07      0.12      0.09        1.00

              Figure 6.5: Representation by race in a city’s juries and population.


    While the proportions in the juries do not precisely represent the population proportions, it is
unclear whether these data provide convincing evidence that the sample is not representative. If the
jurors really were randomly sampled from the registered voters, we might expect small diﬀerences
due to chance. However, unusually large diﬀerences may provide convincing evidence that the juries
were not representative.
   A second application, assessing the ﬁt of a distribution, is presented at the end of this section.
Daily stock returns from the S&P500 for 25 years are used to assess whether stock activity each day
is independent of the stock’s behavior on previous days.
     In these problems, we would like to examine all bins simultaneously, not simply compare one
or two bins at a time, which will require us to develop a new test statistic.


6.3.1  Creating a test statistic for one-way tables



EXAMPLE 6.22
Of the people in the city, 275 served on a jury. If the individuals are randomly selected to serve on a
jury, about how many of the 275 people would we expect to be white? How many would we expect
to be black?

About 72% of the population is white, so we would expect about 72% of the jurors to be white:
0.72 × 275 = 198.

Similarly, we would expect about 7% of the jurors to be black, which would correspond to about
0.07 × 275 = 19.25 black jurors.


GUIDED PRACTICE 6.23
Twelve percent of the population is Hispanic and 9% represent other races. How many of the 275
jurors would we expect to be Hispanic or from another race? Answers can be found in Figure 6.6.


    The sample proportion represented from each race among the 275 jurors was not a precise
match for any ethnic group.  While some sampling variation is expected, we would expect the

---

# OpenIntro Statistics, 4th edition

## 6.3 — Testing for goodness of fit using chi-square

### PDF page 230

230                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA


                        Race               White  Black   Hispanic  Other      Total
                         Observed data         205     26       25       19       275
                         Expected counts       198    19.25     33      24.75      275

                                  Figure 6.6: Actual and expected make-up of the jurors.


             sample proportions to be fairly similar to the population proportions if there is no bias on juries.
         We need to test whether the diﬀerences are strong enough to provide convincing evidence that the
               jurors are not a random sample. These ideas can be organized into hypotheses:

             H0: The jurors are a random sample, i.e. there is no racial bias in who serves on a jury, and the
                   observed counts reﬂect natural sampling ﬂuctuation.

           HA: The jurors are not randomly sampled, i.e. there is racial bias in juror selection.

           To evaluate these hypotheses, we quantify how diﬀerent the observed counts are from the expected
               counts. Strong evidence for the alternative hypothesis would come in the form of unusually large
               deviations in the groups from what would be expected based on sampling variation alone.


            6.3.2  The chi-square test statistic

                   In previous hypothesis tests, we constructed a test statistic of the following form:

                                                 point estimate −null value
                                      SE of point estimate

             This construction was based on (1) identifying the diﬀerence between a point estimate and an
              expected value  if the null hypothesis was true, and (2) standardizing that diﬀerence using the
              standard error of the point estimate. These two ideas will help in the construction of an appropriate
                test statistic for count data.
               Our strategy will be to ﬁrst compute the diﬀerence between the observed counts and the counts
           we would expect if the null hypothesis was true, then we will standardize the diﬀerence:

                                            observed white count −null white count
                                 Z1 =
                                      SE of observed white count

           The standard error for the point estimate of the count in binned data is the square root of the count
             under the null.32 Therefore:

                                                    205 −198
                                           Z1 =  √    = 0.50
                                                       198

           The fraction is very similar to previous test statistics: ﬁrst compute a diﬀerence, then standardize
                     it. These computations should also be completed for the black, Hispanic, and other groups:

                 Black                      Hispanic                  Other
                       26 −19.25                   25 −33                     19 −24.75
                Z2 = √    = 1.54       Z3 = √   = −1.39       Z4 = √    = −1.16
                             19.25                       33                           24.75



         We would like to use a single test statistic to determine if these four standardized diﬀerences are
                irregularly far from zero. That is, Z1, Z2, Z3, and Z4 must be combined somehow to help determine
                      if they – as a group – tend to be unusually far from zero. A ﬁrst thought might be to take the
              absolute value of these four standardized diﬀerences and add them up:

                                                   |Z1| + |Z2| + |Z3| + |Z4| = 4.58

                  32Using some of the rules learned in earlier chapters, we might think that the standard error would be np(1 −p),
               where n is the sample size and p is the proportion in the population. This would be correct if we were looking only
                 at one count. However, we are computing many standardized diﬀerences and adding them together. It can be shown
               – though not here – that the square root of the count is a better way to standardize the count diﬀerences.

---

# OpenIntro Statistics, 4th edition

## 6.3 — Testing for goodness of fit using chi-square

### PDF page 231

6.3. TESTING FOR GOODNESS OF FIT USING CHI-SQUARE                                      231


Indeed, this does give one number summarizing how far the actual counts are from what was expected. However, it is more common to add the squared values:

                            Z21 + Z22 + Z23 + Z24 = 5.89

Squaring each standardized diﬀerence before adding them together does two things:

   • Any standardized diﬀerence that is squared will now be positive.

   • Diﬀerences that already look unusual – e.g. a standardized diﬀerence of 2.5 – will become
    much larger after being squared.

The test statistic X2, which is the sum of the Z2 values, is generally used for these reasons. We can
also write an equation for X2 using the observed counts and null counts:

                       (observed count1 −null count1)2          (observed count4 −null count4)2
         X2 =                 + · · · +
                                     null count1                                  null count4

The ﬁnal number X2 summarizes how strongly the observed counts tend to deviate from the null
counts.  In Section 6.3.4, we will see that  if the null hypothesis is true, then X2 follows a new
distribution called a chi-square distribution.  Using this distribution, we will be able to obtain a
p-value to evaluate the hypotheses.


6.3.3  The chi-square distribution and ﬁnding areas

    The chi-square distribution is sometimes used to characterize data sets and statistics that
are always positive and typically right skewed. Recall a normal distribution had two parameters –
mean and standard deviation – that could be used to describe its exact characteristics. The chisquare distribution has just one parameter called degrees of freedom (df), which inﬂuences the
shape, center, and spread of the distribution.


GUIDED PRACTICE 6.24
Figure 6.7 shows three chi-square distributions.
(a) How does the center of the distribution change when the degrees of freedom is larger?
(b) What about the variability (spread)?
(c) How does the shape change?33



                                                               Degrees of Freedom
                                                                        2
                                                                        4
                                                                        9





            0            5           10           15           20           25

           Figure 6.7: Three chi-square distributions with varying degrees of freedom.


   33(a) The center becomes larger.  If took a careful look, we could see that the mean of each distribution is equal
to the distribution’s degrees of freedom. (b) The variability increases as the degrees of freedom increases.  (c) The
distribution is very strongly skewed for df = 2, and then the distributions become more symmetric for the larger
degrees of freedom df = 4 and df = 9. We would see this trend continue if we examined distributions with even more
larger degrees of freedom.

---

# OpenIntro Statistics, 4th edition

## 6.3 — Testing for goodness of fit using chi-square

### PDF page 232

232                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA


                  Figure 6.7 and Guided Practice 6.24 demonstrate three general properties of chi-square distri-
              butions as the degrees of freedom increases: the distribution becomes more symmetric, the center
            moves to the right, and the variability inﬂates.
               Our principal interest in the chi-square distribution is the calculation of p-values, which (as
           we have seen before) is related to ﬁnding the relevant area in the tail of a distribution. The most
           common ways to do this are using computer software, using a graphing calculator, or using a table.
             For folks wanting to use the table option, we provide an outline of how to read the chi-square table
                in Appendix C.3, which is also where you may ﬁnd the table. For the examples below, use your
               preferred approach to conﬁrm you get the same answers.


          EXAMPLE 6.25
              Figure 6.8(a) shows a chi-square distribution with 3 degrees of freedom and an upper shaded tail
               starting at 6.25. Find the shaded area.

             Using statistical software or a graphing calculator, we can ﬁnd that the upper tail area for a chi-
              square distribution with 3 degrees of freedom (df) and a cutoﬀof 6.25 is 0.1001. That is, the shaded
             upper tail of Figure 6.8(a) has area 0.1.




          EXAMPLE 6.26
              Figure 6.8(b) shows the upper tail of a chi-square distribution with 2 degrees of freedom. The bound
                for this upper tail is at 4.3. Find the tail area.

             Using software, we can ﬁnd that the tail area shaded in Figure 6.8(b) to be 0.1165. If using a table,
           we would only be able to ﬁnd a range of values for the tail area: between 0.1 and 0.2.


          EXAMPLE 6.27
              Figure 6.8(c) shows an upper tail for a chi-square distribution with 5 degrees of freedom and a cutoﬀ
                of 5.1. Find the tail area.

             Using software, we would obtain a tail area of 0.4038. If using the table in Appendix C.3, we would
             have identiﬁed that the tail area is larger than 0.3 but not be able to give the precise value.


           GUIDED PRACTICE 6.28
              Figure 6.8(d) shows a cutoﬀof 11.7 on a chi-square distribution with 7 degrees of freedom. Find the
              area of the upper tail.34




           GUIDED PRACTICE 6.29
              Figure 6.8(e) shows a cutoﬀof 10 on a chi-square distribution with 4 degrees of freedom. Find the
              area of the upper tail.35




           GUIDED PRACTICE 6.30
              Figure 6.8(f) shows a cutoﬀof 9.21 with a chi-square distribution with 3 df. Find the area of the
             upper tail.36





                     34 The area is 0.1109. If using a table, we would identify that it falls between 0.1 and 0.2.
                    35Precise value: 0.0404. If using the table: between 0.02 and 0.05.
                    36Precise value: 0.0266. If using the table: between 0.02 and 0.05.

---

# OpenIntro Statistics, 4th edition

## 6.3 — Testing for goodness of fit using chi-square

### PDF page 233

6.3. TESTING FOR GOODNESS OF FIT USING CHI-SQUARE                                      233





     0              5              10             15         0              5              10             15

                            (a)                                                      (b)





     0        5        10       15       20       25         0        5        10       15       20       25

                             (c)                                                      (d)





     0            5           10           15                 0              5              10             15

                             (e)                                                               (f)


        Figure 6.8:  (a) Chi-square distribution with 3 degrees of freedom, area above
         6.25 shaded. (b) 2 degrees of freedom, area above 4.3 shaded. (c) 5 degrees of
        freedom, area above 5.1 shaded. (d) 7 degrees of freedom, area above 11.7 shaded.
        (e) 4 degrees of freedom, area above 10 shaded.  (f) 3 degrees of freedom, area
        above 9.21 shaded.

---

# OpenIntro Statistics, 4th edition

## 6.3 — Testing for goodness of fit using chi-square

### PDF page 234

234                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA


            6.3.4  Finding a p-value for a chi-square distribution

                   In Section 6.3.2, we identiﬁed a new test statistic (X2) within the context of assessing whether
               there was evidence of racial bias in how jurors were sampled. The null hypothesis represented the
              claim that jurors were randomly sampled and there was no racial bias. The alternative hypothesis
            was that there was racial bias in how the jurors were sampled.
            We determined that a large X2 value would suggest strong evidence favoring the alternative
               hypothesis: that there was racial bias.  However, we could not quantify what the chance was of
              observing such a large test statistic (X2 = 5.89) if the null hypothesis actually was true. This is
             where the chi-square distribution becomes useful. If the null hypothesis was true and there was no
                racial bias, then X2 would follow a chi-square distribution, with three degrees of freedom in this
                case. Under certain conditions, the statistic X2 follows a chi-square distribution with k −1 degrees
                of freedom, where k is the number of bins.


          EXAMPLE 6.31
          How many categories were there in the juror example? How many degrees of freedom should be
               associated with the chi-square distribution used for X2?

              In the jurors example, there were k = 4 categories: white, black, Hispanic, and other. According
               to the rule above, the test statistic X2 should then follow a chi-square distribution with k −1 = 3
              degrees of freedom if H0 is true.


                   Just like we checked sample size conditions to use a normal distribution in earlier sections, we
            must also check a sample size condition to safely apply the chi-square distribution for X2. Each
              expected count must be at least 5. In the juror example, the expected counts were 198, 19.25, 33,
            and 24.75, all easily above 5, so we can apply the chi-square model to the test statistic, X2 = 5.89.


          EXAMPLE 6.32
                   If the null hypothesis is true, the test statistic X2 = 5.89 would be closely associated with a chi-
              square distribution with three degrees of freedom. Using this distribution and test statistic, identify
              the p-value.

           The chi-square distribution and p-value are shown in Figure 6.9. Because larger chi-square values
              correspond to stronger evidence against the null hypothesis, we shade the upper tail to represent
              the p-value. Using statistical software (or the table in Appendix C.3), we can determine that the
              area is 0.1171. Generally we do not reject the null hypothesis with such a large p-value. In other
              words, the data do not provide convincing evidence of racial bias in the juror selection.





                                    0           5           10          15

                      Figure 6.9: The p-value for the juror hypothesis test is shaded in the chi-square
                        distribution with df = 3.

---

# OpenIntro Statistics, 4th edition

## 6.3 — Testing for goodness of fit using chi-square

### PDF page 235

6.3. TESTING FOR GOODNESS OF FIT USING CHI-SQUARE                                      235



  CHI-SQUARE TEST FOR ONE-WAY TABLE
  Suppose we are to evaluate whether there is convincing evidence that a set of observed counts
  O1, O2, ..., Ok in k categories are unusually diﬀerent from what might be expected under a null
  hypothesis. Call the expected counts that are based on the null hypothesis E1, E2, ..., Ek.  If
  each expected count is at least 5 and the null hypothesis is true, then the test statistic below
  follows a chi-square distribution with k −1 degrees of freedom:

                         (O1 −E1)2   (O2 −E2)2       (Ok −Ek)2
                X2 =       +       + · · · +
                          E1         E2             Ek

  The p-value for this test statistic is found by looking at the upper tail of this chi-square distri-
  bution. We consider the upper tail because larger values of X2 would provide greater evidence
  against the null hypothesis.



  CONDITIONS FOR THE CHI-SQUARE TEST
  There are two conditions that must be checked before performing a chi-square test:

  Independence. Each case that contributes a count to the table must be independent of all
        the other cases in the table.

  Sample size / distribution. Each particular scenario (i.e.  cell count) must have at least
       5 expected cases.

  Failing to check conditions may aﬀect the test’s error rates.


   When examining a table with just two bins, pick a single bin and use the one-proportion
methods introduced in Section 6.1.

---

# OpenIntro Statistics, 4th edition

## 6.3 — Testing for goodness of fit using chi-square

### PDF page 236

236                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA


            6.3.5  Evaluating goodness of ﬁt for a distribution

                   Section 4.2 would be useful background reading for this example, but it is not a prerequisite.
            We can apply the chi-square testing framework to the second problem in this section: evaluating
             whether a certain statistical model ﬁts a data set. Daily stock returns from the S&P500 for 10 can
             be used to assess whether stock activity each day is independent of the stock’s behavior on previous
               days. This sounds like a very complex question, and it is, but a chi-square test can be used to study
              the problem. We will label each day as Up or Down (D) depending on whether the market was up
               or down that day. For example, consider the following changes in price, their new labels of up and
             down, and then the number of days that must be observed before each Up day:

                       Change in price      2.52   -1.46   0.51   -4.07   3.36   1.10   -5.46   -1.03   -2.99   1.71
                      Outcome         Up   D    Up   D    Up   Up   D    D    D    Up
                       Days to Up          1         -      2         -      2     1         -          -          -      4

                    If the days really are independent, then the number of days until a positive trading day should follow
             a geometric distribution. The geometric distribution describes the probability of waiting for the kth
                  trial to observe the ﬁrst success. Here each up day (Up) represents a success, and down (D) days
               represent failures. In the data above, it took only one day until the market was up, so the ﬁrst wait
             time was 1 day. It took two more days before we observed our next Up trading day, and two more
                for the third Up day. We would like to determine if these counts (1, 2, 2, 1, 4, and so on) follow
              the geometric distribution. Figure 6.10 shows the number of waiting days for a positive trading day
              during 10 years for the S&P500.

                          Days           1    2    3    4   5   6  7+      Total
                            Observed      717  369  155  69  28  14   10      1362

                      Figure 6.10: Observed distribution of the waiting time until a positive trading day
                          for the S&P500.

            We consider how many days one must wait until observing an Up day on the S&P500 stock
               index.  If the stock activity was independent from one day to the next and the probability of a
               positive trading day was constant, then we would expect this waiting time to follow a geometric
                distribution. We can organize this into a hypothesis framework:

             H0: The stock market being up or down on a given day is independent from all other days. We
                       will consider the number of days that pass until an Up day is observed. Under this hypothesis,
                   the number of days until an Up day should follow a geometric distribution.

           HA: The stock market being up or down on a given day is not independent from all other days.
                    Since we know the number of days until an Up day would follow a geometric distribution under
                   the null, we look for deviations from the geometric distribution, which would support the
                     alternative hypothesis.

             There are important implications in our result for stock traders:  if information from past trading
             days is useful in telling what will happen today, that information may provide an advantage over
              other traders.
            We consider data for the S&P500 and summarize the waiting times in Figure 6.11 and Fig-
              ure 6.12. The S&P500 was positive on 54.5% of those days.
                 Because applying the chi-square framework requires expected counts to be at least 5, we have
              binned together all the cases where the waiting time was at least 7 days to ensure each expected
             count is well above this minimum. The actual data, shown in the Observed row in Figure 6.11, can
             be compared to the expected counts from the Geometric Model row. The method for computing
              expected counts is discussed in Figure 6.11.  In general, the expected counts are determined by
               (1) identifying the null proportion associated with each bin, then (2) multiplying each null proportion
            by the total count to obtain the expected counts. That is, this strategy identiﬁes what proportion
                of the total count we would expect to be in each bin.

---

# OpenIntro Statistics, 4th edition

## 6.3 — Testing for goodness of fit using chi-square

### PDF page 237

6.3. TESTING FOR GOODNESS OF FIT USING CHI-SQUARE                                      237





           Days                 1    2    3    4   5   6  7+      Total
            Observed            717  369  155  69  28  14   10      1362
            Geometric Model     743  338  154  70  32  14   12      1362

        Figure 6.11: Distribution of the waiting time until a positive trading day. The
        expected counts based on the geometric model are shown in the last row.  To
       ﬁnd each expected count, we identify the probability of waiting D days based on
        the geometric model (P(D) = (1 −0.545)D−1(0.545)) and multiply by the total
       number of streaks, 1362.  For example, waiting for three days occurs under the
        geometric model about 0.4552 × 0.545 = 11.28% of the time, which corresponds to
        0.1128 × 1362 = 154 streaks.





           800                                                                         Observed
                                                                            Expected

           600


           400                         Frequency

           200


             0

                      1        2        3        4        5        6       7+
                                            Wait Until Positive Day

        Figure 6.12: Side-by-side bar plot of the observed and expected counts for each
        waiting time.

---

# OpenIntro Statistics, 4th edition

## 6.3 — Testing for goodness of fit using chi-square

### PDF page 238

238                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA



          EXAMPLE 6.33
          Do you notice any unusually large deviations in the graph? Can you tell if these deviations are due
               to chance just by looking?

                 It is not obvious whether diﬀerences in the observed counts and the expected counts from the geo-
              metric distribution are signiﬁcantly diﬀerent. That is, it is not clear whether these deviations might
             be due to chance or whether they are so strong that the data provide convincing evidence against
              the null hypothesis. However, we can perform a chi-square test using the counts in Figure 6.11.


           GUIDED PRACTICE 6.34
              Figure 6.11 provides a set of count data for waiting times (O1 = 717, O2 = 369, ...) and expected
              counts under the geometric distribution (E1 = 743, E2 = 338, ...). Compute the chi-square test
                 statistic, X2.37




           GUIDED PRACTICE 6.35
             Because the expected counts are all at least 5, we can safely apply the chi-square distribution to
            X2. However, how many degrees of freedom should we use?38




          EXAMPLE 6.36
                   If the observed counts follow the geometric model, then the chi-square test statistic X2 = 4.61 would
                closely follow a chi-square distribution with df = 6. Using this information, compute a p-value.

              Figure 6.13 shows the chi-square distribution, cutoﬀ, and the shaded p-value. Using software, we
             can ﬁnd the p-value: 0.5951. Ultimately, we do not have suﬃcient evidence to reject the notion that
              the wait times follow a geometric distribution for the last 10 years of data for the S&P500, i.e. we
             cannot reject the notion that trading days are independent.





                                                                          Area representing
                                                                                    the p−value




                               0           5           10          15          20          25

                      Figure 6.13: Chi-square distribution with 6 degrees of freedom. The p-value for
                      the stock analysis is shaded.



          EXAMPLE 6.37
              In Example 6.36, we did not reject the null hypothesis that the trading days are independent during
              the last 10 of data. Why is this so important?

                 It may be tempting to think the market is “due” for an Up day if there have been several consecutive
             days where it has been down. However, we haven’t found strong evidence that there’s any such
              property where the market is “due” for a correction. At the very least, the analysis suggests any
             dependence between days is very weak.

                37X2 = (717−743)2743  + (369−338)2338  + · · · + (10−12)212  = 4.61
                  38There are k = 7 groups, so we use df = k −1 = 6.

---

# OpenIntro Statistics, 4th edition

## 6.3 — Testing for goodness of fit using chi-square

### PDF page 239

6.3. TESTING FOR GOODNESS OF FIT USING CHI-SQUARE                                      239


Exercises


6.31  True or false, Part I. Determine if the statements below are true or false. For each false statement,
suggest an alternative wording to make it a true statement.

(a) The chi-square distribution, just like the normal distribution, has two parameters, mean and standard
    deviation.
(b) The chi-square distribution is always right skewed, regardless of the value of the degrees of freedom
    parameter.
(c) The chi-square statistic is always positive.
(d) As the degrees of freedom increases, the shape of the chi-square distribution becomes more skewed.

6.32  True or false, Part II. Determine if the statements below are true or false. For each false statement,
suggest an alternative wording to make it a true statement.

(a) As the degrees of freedom increases, the mean of the chi-square distribution increases.
(b)  If you found χ2 = 10 with df = 5 you would fail to reject H0 at the 5% signiﬁcance level.
(c) When ﬁnding the p-value of a chi-square test, we always shade the tail areas in both tails.
(d) As the degrees of freedom increases, the variability of the chi-square distribution decreases.

6.33  Open source textbook. A professor using an open source introductory statistics book predicts that
60% of the students will purchase a hard copy of the book, 25% will print it out from the web, and 15%
will read it online. At the end of the semester he asks his students to complete a survey where they indicate
what format of the book they used. Of the 126 students, 71 said they bought a hard copy of the book, 30
said they printed it out from the web, and 25 said they read it online.

(a) State the hypotheses for testing if the professor’s predictions were inaccurate.
(b) How many students did the professor expect to buy the book, print the book, and read the book
    exclusively online?
(c) This is an appropriate setting for a chi-square test. List the conditions required for a test and verify
    they are satisﬁed.
(d) Calculate the chi-squared statistic, the degrees of freedom associated with it, and the p-value.
(e) Based on the p-value calculated in part (d), what is the conclusion of the hypothesis test?  Interpret
    your conclusion in this context.

6.34  Barking deer. Microhabitat factors associated with forage and bed sites of barking deer in Hainan
Island, China were examined. In this region woods make up 4.8% of the land, cultivated grass plot makes
up 14.7%, and deciduous forests make up 39.6%. Of the 426 sites where the deer forage, 4 were categorized
as woods, 16 as cultivated grassplot, and 61 as deciduous forests. The table below summarizes these data.39

               Woods   Cultivated grassplot   Deciduous forests   Other   Total
                    4             16                 61          345    426




(a) Write the hypotheses for testing if barking deer prefer to forage in cer-
    tain habitats over others.
(b) What type of test can we use to answer this research question?
(c) Check if the assumptions and conditions required for this test are sat-
    isﬁed.
(d) Do these data provide convincing evidence that barking deer prefer to
    forage in certain habitats over others? Conduct an appropriate hypoth-
     esis test to answer this research question.                                   Photo by Shrikant Rao
                                                                                     (http://ﬂic.kr/p/4Xjdkk)
                                                         CC BY 2.0 license





   39Liwei Teng et al. “Forage and bed sites characteristics of Indian muntjac (Muntiacus muntjak) in Hainan Island,
China”. In: Ecological Research 19.6 (2004), pp. 675–681.

---

# OpenIntro Statistics, 4th edition

## 6.4 — Testing for independence in two-way tables

### PDF page 240

240                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA


        6.4  Testing for independence in two-way tables



            We all buy used products – cars, computers, textbooks, and so on – and we sometimes assume
              the sellers of those products will be forthright about any underlying problems with what they’re
                 selling. This is not something we should take for granted. Researchers recruited 219 participants in
             a study where they would sell a used iPod40 that was known to have frozen twice in the past. The
               participants were incentivized to get as much money as they could for the iPod since they would
               receive a 5% cut of the sale on top of $10 for participating. The researchers wanted to understand
            what types of questions would elicit the seller to disclose the freezing issue.
                Unbeknownst to the participants who were the sellers in the study, the buyers were collaborating
             with the researchers to evaluate the inﬂuence of diﬀerent questions on the likelihood of getting the
                 sellers to disclose the past issues with the iPod. The scripted buyers started with “Okay, I guess I’m
             supposed to go ﬁrst. So you’ve had the iPod for 2 years ...” and ended with one of three questions:

                • General: What can you tell me about it?

                • Positive Assumption: It doesn’t have any problems, does it?

                • Negative Assumption: What problems does it have?

           The question is the treatment given to the sellers, and the response is whether the question prompted
            them to disclose the freezing issue with the iPod. The results are shown in Figure 6.14, and the
             data suggest that asking the, What problems does it have?, was the most eﬀective at getting the
                  seller to disclose the past freezing issues. However, you should also be asking yourself: could we see
               these results due to chance alone, or is this in fact evidence that some questions are more eﬀective
                for getting at the truth?

                                       General   Positive Assumption   Negative Assumption   Total
                       Disclose Problem     2             23                   36           61
                    Hide Problem        71             50                   37           158
                      Total               73             73                   73           219

                      Figure 6.14: Summary of the iPod study, where a question was posed to the study
                        participant who acted




             DIFFERENCES OF ONE-WAY TABLES VS TWO-WAY TABLES
          A one-way table describes counts for each outcome in a single variable. A two-way table
                 describes counts for combinations of outcomes for two variables. When we consider a two-way
                  table, we often would like to know, are these variables related in any way? That is, are they
               dependent (versus independent)?


               The hypothesis test for the iPod experiment is really about assessing whether there is statis-
                 tically signiﬁcant evidence that the success each question had on getting the participant to disclose
              the problem with the iPod. In other words, the goal is to check whether the buyer’s question was
             independent of whether the seller disclosed a problem.





                   40For readers not as old as the authors, an iPod is basically an iPhone without any cellular service, assuming it
              was one of the later generations. Earlier generations were more basic.

---

# OpenIntro Statistics, 4th edition

## 6.4 — Testing for independence in two-way tables

### PDF page 241

6.4. TESTING FOR INDEPENDENCE IN TWO-WAY TABLES                                      241


6.4.1  Expected counts in two-way tables

Like with one-way tables, we will need to compute estimated counts for each cell in a two-way table.


EXAMPLE 6.38
From the experiment, we can compute the proportion of all sellers who disclosed the freezing problem
as 61/219 = 0.2785. If there really is no diﬀerence among the questions and 27.85% of sellers were
going to disclose the freezing problem no matter the question that was put to them, how many of
the 73 people in the General group would we have expected to disclose the freezing problem?

We would predict that 0.2785×73 = 20.33 sellers would disclose the problem. Obviously we observed
fewer than this, though it is not yet clear if that is due to chance variation or whether that is because
the questions vary in how eﬀective they are at getting to the truth.


GUIDED PRACTICE 6.39
 If the questions were actually equally eﬀective, meaning about 27.85% of respondents would disclose
the freezing issue regardless of what question they were asked, about how many sellers would we
expect to hide the freezing problem from the Positive Assumption group?41


   We can compute the expected number of sellers who we would expect to disclose or hide the
freezing issue for all groups, if the questions had no impact on what they disclosed, using the same
strategy employed in Example 6.38 and Guided Practice 6.39. These expected counts were used to
construct Figure 6.15, which is the same as Figure 6.14, except now the expected counts have been
added in parentheses.

                        General     Positive Assumption   Negative Assumption   Total
       Disclose Problem  2  (20.33)   23 (20.33)            36 (20.33)            61
      Hide Problem     71 (52.67)  50 (52.67)            37 (52.67)            158
       Total             73         73                  73                   219

                Figure 6.15: The observed counts and the (expected counts).


    The examples and exercises above provided some help in computing expected counts. In general,
expected counts for a two-way table may be computed using the row totals, column totals, and the
table total. For instance, if there was no diﬀerence between the groups, then about 27.85% of each
column should be in the ﬁrst row:

                               0.2785 × (column 1 total) = 20.33
                               0.2785 × (column 2 total) = 20.33
                               0.2785 × (column 3 total) = 20.33

Looking back to how 0.2785 was computed – as the fraction of sellers who disclosed the freezing
issue (158/219) – these three expected counts could have been computed as

                          row 1 total
                                       (column 1 total) = 20.33
                                table total
                          row 1 total
                                       (column 2 total) = 20.33
                                table total
                          row 1 total
                                       (column 3 total) = 20.33
                                table total

This leads us to a general formula for computing expected counts in a two-way table when we would
like to test whether there is strong evidence of an association between the column variable and row
variable.

  41We would expect (1 −0.2785) × 73 = 52.67. It is okay that this result, like the result from Example 6.38, is a
fraction.

---

# OpenIntro Statistics, 4th edition

## 6.4 — Testing for independence in two-way tables

### PDF page 242

242                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA



            COMPUTING EXPECTED COUNTS IN A TWO-WAY TABLE
             To identify the expected count for the ith row and jth column, compute

                                                        (row i total) × (column j total)
                             Expected Countrow i, col j =
                                                                          table total



            6.4.2  The chi-square test for two-way tables

               The chi-square test statistic for a two-way table is found the same way it is found for a one-way
                table. For each table count, compute

                                                          (observed count −expected count)2
                           General formula
                                                                  expected count
                                                             (2 −20.33)2
                     Row 1, Col 1                  = 16.53
                                                               20.33
                                                           (23 −20.33)2
                     Row 1, Col 2                  = 0.35
                                                               20.33
                                                                                                                                                                          ...                                                                                                                                                              ...
                                                           (37 −52.67)2
                     Row 2, Col 3                  = 4.66
                                                               52.67

            Adding the computed value for each cell gives the chi-square test statistic X2:

                              X2 = 16.53 + 0.35 + · · · + 4.66 = 40.13

              Just like before, this test statistic follows a chi-square distribution. However, the degrees of freedom
               are computed a little diﬀerently for a two-way table.42 For two way tables, the degrees of freedom
                   is equal to

                                  df = (number of rows minus 1) × (number of columns minus 1)

              In our example, the degrees of freedom parameter is

                                                     df = (2 −1) × (3 −1) = 2

                    If the null hypothesis is true (i.e. the questions had no impact on the sellers in the experiment),
             then the test statistic X2 = 40.13 closely follows a chi-square distribution with 2 degrees of freedom.
             Using this information, we can compute the p-value for the test, which is depicted in Figure 6.16.


            COMPUTING DEGREES OF FREEDOM FOR A TWO-WAY TABLE
            When applying the chi-square test to a two-way table, we use

                                                       df = (R −1) × (C −1)

               where R is the number of rows in the table and C is the number of columns.


             When analyzing 2-by-2 contingency tables, one guideline is to use the two-proportion methods
              introduced in Section 6.2.





                     42Recall: in the one-way table, the degrees of freedom was the number of cells minus 1.

---

# OpenIntro Statistics, 4th edition

## 6.4 — Testing for independence in two-way tables

### PDF page 243

6.4. TESTING FOR INDEPENDENCE IN TWO-WAY TABLES                                      243





                                                                    Tail area (1 / 500 million)
                                                                          is too small to see

                  0        10       20       30       40       50

              Figure 6.16: Visualization of the p-value for X2 = 40.13 when df = 2.



EXAMPLE 6.40
Find the p-value and draw a conclusion about whether the question aﬀects the sellers likelihood of
reporting the freezing problem.

Using a computer, we can compute a very precise value for the tail area above X2 = 40.13 for a
chi-square distribution with 2 degrees of freedom: 0.000000002. (If using the table in Appendix C.3,
we would identify the p-value is smaller than 0.001.) Using a signiﬁcance level of α = 0.05, the null
hypothesis is rejected since the p-value is smaller. That is, the data provide convincing evidence that
the question asked did aﬀect a seller’s likelihood to tell the truth about problems with the iPod.




EXAMPLE 6.41
Figure 6.17 summarizes the results of an experiment evaluating three treatments for Type 2 Diabetes
in patients aged 10-17 who were being treated with metformin. The three treatments considered
were continued treatment with metformin (met), treatment with metformin combined with rosiglitazone (rosi), or a lifestyle intervention program. Each patient had a primary outcome, which was
either lacked glycemic control (failure) or did not lack that control (success). What are appropriate
hypotheses for this test?


 H0: There is no diﬀerence in the eﬀectiveness of the three treatments.

HA: There is some diﬀerence in eﬀectiveness between the three treatments, e.g. perhaps the rosi
     treatment performed better than lifestyle.



                                            Failure   Success   Total
                         lifestyle    109      125     234
                         met          120      112     232
                         rosi          90      143     233
                             Total         319      380     699

                      Figure 6.17: Results for the Type 2 Diabetes study.

---

# OpenIntro Statistics, 4th edition

## 6.4 — Testing for independence in two-way tables

### PDF page 244

244                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA



           GUIDED PRACTICE 6.42
         A chi-square test for a two-way table may be used to test the hypotheses in Example 6.41. As a
               ﬁrst step, compute the expected values for each of the six table cells.43




           GUIDED PRACTICE 6.43
           Compute the chi-square test statistic for the data in Figure 6.17.44




           GUIDED PRACTICE 6.44
             Because there are 3 rows and 2 columns, the degrees of freedom for the test is df = (3−1)×(2−1) = 2.
            Use X2 = 8.16, df = 2, evaluate whether to reject the null hypothesis using a signiﬁcance level
                of 0.05.45





                 43The expected count for row one / column one is found by multiplying the row one total (234) and column one
                   total (319), then dividing by the table total (699): 234×319699  = 106.8. Similarly for the second column and the ﬁrst
                row: 234×380699  = 127.2. Row 2: 105.9 and 126.1. Row 3: 106.3 and 126.7.
                   44For each cell, compute (obs−exp)2exp      . For instance, the ﬁrst row and ﬁrst column: (109−106.8)2106.8   = 0.05. Adding the
                   results of each cell gives the chi-square test statistic: X2 = 0.05 + · · · + 2.11 = 8.16.
                     45 If using a computer, we can identify the p-value as 0.017. That is, we reject the null hypothesis because the
                 p-value is less than 0.05, and we conclude that at least one of the treatments is more or less eﬀective than the others
                 at treating Type 2 Diabetes for glycemic control.

---

# OpenIntro Statistics, 4th edition

## 6.4 — Testing for independence in two-way tables

### PDF page 245

6.4. TESTING FOR INDEPENDENCE IN TWO-WAY TABLES                                      245


Exercises


6.35  Quitters. Does being part of a support group aﬀect the ability of people to quit smoking? A county
health department enrolled 300 smokers in a randomized experiment. 150 participants were assigned to a
group that used a nicotine patch and met weekly with a support group; the other 150 received the patch
and did not meet with a support group. At the end of the study, 40 of the participants in the patch plus
support group had quit smoking while only 30 smokers had quit in the other group.

(a) Create a two-way table presenting the results of this study.
(b) Answer each of the following questions under the null hypothesis that being part of a support group does
    not aﬀect the ability of people to quit smoking, and indicate whether the expected values are higher or
    lower than the observed values.

          i. How many subjects in the “patch + support” group would you expect to quit?
         ii. How many subjects in the “patch only” group would you expect to not quit?

6.36  Full body scan, Part II. The table below summarizes a data set we ﬁrst encountered in Exercise 6.26
regarding views on full-body scans and political aﬃliation. The diﬀerences in each political group may be
due to chance. Complete the following computations under the null hypothesis of independence between an
individual’s party aﬃliation and his support of full-body scans.  It may be useful to ﬁrst add on an extra
column for row totals before proceeding with the computations.

                                                          Party Aﬃliation
                                               Republican  Democrat   Independent
                       Should                    264         299         351
             Answer   Should not                 38          55          77
                       Don’t know/No answer      16          15          22
                         Total                      318         369         450

(a) How many Republicans would you expect to not support the use of full-body scans?
(b) How many Democrats would you expect to support the use of full- body scans?
(c) How many Independents would you expect to not know or not answer?

6.37  Offshore drilling, Part III. The table below summarizes a data set we ﬁrst encountered in Exercise 6.23
that examines the responses of a random sample of college graduates and non-graduates on the topic of oil
drilling.  Complete a chi-square test for these data to check whether there is a statistically signiﬁcant
diﬀerence in responses from college graduates and non-graduates.

                                                      College Grad
                                                Yes   No
                                  Support       154    132
                                Oppose       180    126
                           Do not know   104    131
                                     Total         438    389

6.38  Parasitic worm. Lymphatic ﬁlariasis is a disease caused by a parasitic worm. Complications of the
disease can lead to extreme swelling and other complications. Here we consider results from a randomized
experiment that compared three diﬀerent drug treatment options to clear people of the this parasite, which
people are working to eliminate entirely. The results for the second year of the study are given below:46

                                           Clear at Year 2  Not Clear at Year 2
                    Three drugs               52                 2
                Two drugs                31                24
                Two drugs annually        42                14

(a) Set up hypotheses for evaluating whether there is any diﬀerence in the performance of the treatments,
   and also check conditions.
(b) Statistical software was used to run a chi-square test, which output:

               X2 = 23.7                  df = 2                 p-value = 7.2e-6

    Use these results to evaluate the hypotheses from part (a), and provide a conclusion in the context of
    the problem.


   46Christopher King et al. “A Trial of a Triple-Drug Treatment for Lymphatic Filariasis”. In: New England Journal
of Medicine 379 (2018), pp. 1801–1810.

---

# OpenIntro Statistics, 4th edition

## 6.4 — Testing for independence in two-way tables

### PDF page 246

246                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA


       Chapter exercises



               6.39  Active learning. A teacher wanting to increase the active learning component of her course is con-
               cerned about student reactions to changes she is planning to make. She conducts a survey in her class,
               asking students whether they believe more active learning in the classroom (hands on exercises) instead of
                 traditional lecture will helps improve their learning. She does this at the beginning and end of the semester
             and wants to evaluate whether students’ opinions have changed over the semester. Can she used the methods
            we learned in this chapter for this analysis? Explain your reasoning.

               6.40  Website experiment. The OpenIntro website occasionally experiments with design and link place-
              ment. We conducted one experiment testing three diﬀerent placements of a download link for this textbook
             on the book’s main page to see which location, if any, led to the most downloads. The number of site visitors
               included in the experiment was 701 and is captured in one of the response combinations in the following
                 table:

                                                   Download  No Download
                                                 Position 1    13.8%       18.3%
                                                 Position 2    14.6%       18.5%
                                                 Position 3    12.1%       22.7%

                (a) Calculate the actual number of site visitors in each of the six response categories.
                (b) Each individual in the experiment had an equal chance of being in any of the three experiment groups.
                  However, we see that there are slightly diﬀerent totals for the groups.  Is there any evidence that the
                  groups were actually imbalanced? Make sure to clearly state hypotheses, check conditions, calculate the
                   appropriate test statistic and the p-value, and make your conclusion in context of the data.
                 (c) Complete an appropriate hypothesis test to check whether there is evidence that there is a higher rate
                      of site visitors clicking on the textbook link in any of the three groups.

               6.41  Shipping holiday gifts. A local news survey asked 500 randomly sampled Los Angeles residents
              which shipping carrier they prefer to use for shipping holiday gifts. The table below shows the distribution
                 of responses by age group as well as the expected counts for each cell (shown in parentheses).

                                                                   Age
                                                                18-34       35-54      55+     Total
                                 USPS           72    (81)   97    (102)   76    (62)   245
                                UPS            52    (53)   76    (68)   34    (41)   162
                           Shipping Method   FedEx          31    (21)   24    (27)    9     (16)    64
                                         Something else   7     (5)    6      (7)    3     (4)    16
                                       Not sure         3     (5)    6      (5)    4     (3)    13
                                              Total              165         209         126      500

                (a) State the null and alternative hypotheses for testing for independence of age and preferred shipping
                method for holiday gifts among Los Angeles residents.
                (b) Are the conditions for inference using a chi-square test satisﬁed?

               6.42  The Civil War. A national survey conducted among a simple random sample of 1,507 adults shows
               that 56% of Americans think the Civil War is still relevant to American politics and political life.47

                (a) Conduct a hypothesis test to determine if these data provide strong evidence that the majority of the
                 Americans think the Civil War is still relevant.
                (b) Interpret the p-value in this context.
                 (c) Calculate a 90% conﬁdence interval for the proportion of Americans who think the Civil War is still
                     relevant. Interpret the interval in this context, and comment on whether or not the conﬁdence interval
                    agrees with the conclusion of the hypothesis test.





                47Pew Research Center Publications, Civil War at 150: Still Relevant, Still Divisive, data collected between March
               30 - April 3, 2011.

---

# OpenIntro Statistics, 4th edition

## 6.4 — Testing for independence in two-way tables

### PDF page 247

6.4. TESTING FOR INDEPENDENCE IN TWO-WAY TABLES                                      247


6.43  College smokers. We are interested in estimating the proportion of students at a university who
smoke. Out of a random sample of 200 students from this university, 40 students smoke.

(a) Calculate a 95% conﬁdence interval for the proportion of students at this university who smoke, and
    interpret this interval in context. (Reminder: Check conditions.)
(b)  If we wanted the margin of error to be no larger than 2% at a 95% conﬁdence level for the proportion
     of students who smoke, how big of a sample would we need?

6.44  Acetaminophen and liver damage.  It is believed that large doses of acetaminophen (the active
ingredient in over the counter pain relievers like Tylenol) may cause damage to the liver. A researcher
wants to conduct a study to estimate the proportion of acetaminophen users who have liver damage. For
participating in this study, he will pay each subject $20 and provide a free medical consultation if the patient
has liver damage.

(a)  If he wants to limit the margin of error of his 98% conﬁdence interval to 2%, what is the minimum
   amount of money he needs to set aside to pay his subjects?
(b) The amount you calculated in part (a) is substantially over his budget so he decides to use fewer subjects.
   How will this aﬀect the width of his conﬁdence interval?

6.45  Life after college. We are interested in estimating the proportion of graduates at a mid-sized university who found a job within one year of completing their undergraduate degree. Suppose we conduct a
survey and ﬁnd out that 348 of the 400 randomly sampled graduates found jobs. The graduating class under
consideration included over 4500 students.

(a) Describe the population parameter of interest. What is the value of the point estimate of this parameter?
(b) Check if the conditions for constructing a conﬁdence interval based on these data are met.
(c) Calculate a 95% conﬁdence interval for the proportion of graduates who found a job within one year of
    completing their undergraduate degree at this university, and interpret it in the context of the data.
(d) What does “95% conﬁdence” mean?
(e) Now calculate a 99% conﬁdence interval for the same parameter and interpret it in the context of the
    data.
(f) Compare the widths of the 95% and 99% conﬁdence intervals. Which one is wider? Explain.

6.46  Diabetes and unemployment. A Gallup poll surveyed Americans about their employment status
and whether or not they have diabetes. The survey results indicate that 1.5% of the 47,774 employed (full
or part time) and 2.5% of the 5,855 unemployed 18-29 year olds have diabetes.48

(a) Create a two-way table presenting the results of this study.
(b) State appropriate hypotheses to test for diﬀerence in proportions of diabetes between employed and
    unemployed Americans.
(c) The sample diﬀerence is about 1%. If we completed the hypothesis test, we would ﬁnd that the p-value
      is very small (about 0), meaning the diﬀerence is statistically signiﬁcant. Use this result to explain the
    diﬀerence between statistically signiﬁcant and practically signiﬁcant ﬁndings.

6.47  Rock-paper-scissors.  Rock-paper-scissors is a hand game played by two or more people where
players choose to sign either rock, paper, or scissors with their hands. For your statistics class project, you
want to evaluate whether players choose between these three options randomly, or if certain options are
favored above others. You ask two friends to play rock-paper-scissors and count the times each option is
played. The following table summarizes the data:

                                 Rock   Paper   Scissors
                                     43     21       35

Use these data to evaluate whether players choose between these three options randomly, or if certain options
are favored above others. Make sure to clearly outline each step of your analysis, and interpret your results
in context of the data and the research question.





   48Gallup Wellbeing, Employed Americans in Better Health Than the Unemployed, data collected Jan. 2, 2011 -
May 21, 2012.

---

# OpenIntro Statistics, 4th edition

## 6.4 — Testing for independence in two-way tables

### PDF page 248

248                              CHAPTER 6. INFERENCE FOR CATEGORICAL DATA


               6.48  2010 Healthcare Law. On June 28, 2012 the U.S. Supreme Court upheld the much debated 2010
                healthcare law, declaring it constitutional. A Gallup poll released the day after this decision indicates that
            46% of 1,012 Americans agree with this decision. At a 95% conﬁdence level, this sample has a 3% margin of
                  error. Based on this information, determine if the following statements are true or false, and explain your
                reasoning.49

                (a) We are 95% conﬁdent that between 43% and 49% of Americans in this sample support the decision of
                   the U.S. Supreme Court on the 2010 healthcare law.
                (b) We are 95% conﬁdent that between 43% and 49% of Americans support the decision of the U.S. Supreme
                 Court on the 2010 healthcare law.
                 (c)  If we considered many random samples of 1,012 Americans, and we calculated the sample proportions
                      of those who support the decision of the U.S. Supreme Court, 95% of those sample proportions will be
                  between 43% and 49%.
                (d) The margin of error at a 90% conﬁdence level would be higher than 3%.

               6.49  Browsing on the mobile device. A survey of 2,254 American adults indicates that 17% of cell phone
              owners browse the internet exclusively on their phone rather than a computer or other device.50

                (a) According to an online article, a report from a mobile research company indicates that 38 percent of
                  Chinese mobile web users only access the internet through their cell phones.51 Conduct a hypothesis
                      test to determine if these data provide strong evidence that the proportion of Americans who only use
                     their cell phones to access the internet is diﬀerent than the Chinese proportion of 38%.
                (b) Interpret the p-value in this context.
                 (c) Calculate a 95% conﬁdence interval for the proportion of Americans who access the internet on their
                        cell phones, and interpret the interval in this context.

               6.50  Coffee and Depression. Researchers conducted a study investigating the relationship between caf-
                feinated coﬀee consumption and risk of depression in women. They collected data on 50,739 women free of
                depression symptoms at the start of the study in the year 1996, and these women were followed through 2006.
            The researchers used questionnaires to collect data on caﬀeinated coﬀee consumption, asked each individual
              about physician- diagnosed depression, and also asked about the use of antidepressants. The table below
              shows the distribution of incidences of depression by amount of caﬀeinated coﬀee consumption.52
                                                      Caﬀeinated coﬀee consumption
                             ≤1          2-6         1         2-3     ≥4
                                       cup/week   cups/week   cup/day   cups/day   cups/day    Total
                          Clinical     Yes          670        373        905        564         95    2,607
                        depression  No        11,545        6,244     16,329     11,726       2,288   48,132
                                    Total      12,215        6,617     17,234     12,290       2,383   50,739

                (a) What type of test is appropriate for evaluating  if there is an association between coﬀee intake and
                    depression?
                (b) Write the hypotheses for the test you identiﬁed in part (a).
                 (c) Calculate the overall proportion of women who do and do not suﬀer from depression.
                (d) Identify the expected count for the highlighted cell, and calculate the contribution of this cell to the test
                        statistic, i.e. (Observed −Expected)2/Expected.
                 (e) The test statistic is χ2 = 20.93. What is the p-value?
                  (f) What is the conclusion of the hypothesis test?
                (g) One of the authors of this study was quoted on the NYTimes as saying it was “too early to recommend
                   that women load up on extra coﬀee” based on just this study.53 Do you agree with this statement?
                  Explain your reasoning.





                   49Gallup, Americans Issue Split Decision on Healthcare Ruling, data collected June 28, 2012.
                50Pew Internet, Cell Internet Use 2012, data collected between March 15 - April 13, 2012.
                    51S. Chang. “The Chinese Love to Use Feature Phone to Access the Internet”. In: M.I.C Gadget (2012).
                 52M. Lucas et al. “Coﬀee, caﬀeine, and risk of depression among women”. In: Archives of internal medicine 171.17
                  (2011), p. 1571.
                  53A. O’Connor. “Coﬀee Drinking Linked to Less Depression in Women”. In: New York Times (2011).

---

# OpenIntro Statistics, 4th edition

## 7.1 — One-sample means with the t-distribution

### PDF page 249

249

Chapter 7

Inference for numerical data





7.1 One-sample means with the t-distribution

7.2 Paired data

7.3 Difference of two means

7.4 Power calculations for a difference of means

7.5 Comparing many means with ANOVA

---

# OpenIntro Statistics, 4th edition

## 7.1 — One-sample means with the t-distribution

### PDF page 250

250





         Chapter 5 introduced a framework for statistical inference based on

         conﬁdence intervals and hypotheses using the normal distribution for

         sample proportions.  In this chapter, we encounter several new point

          estimates and a couple new distributions. In each case, the inference

           ideas remain the same: determine which point estimate or test statistic

              is useful, identify an appropriate distribution for the point estimate or

           test statistic, and apply the ideas of inference.





         For videos, slides, and other resources, please visit
        www.openintro.org/os

---

# OpenIntro Statistics, 4th edition

## 7.1 — One-sample means with the t-distribution

### PDF page 251

7.1. ONE-SAMPLE MEANS WITH THE T-DISTRIBUTION                                         251


7.1  One-sample means with the t-distribution



Similar to how we can model the behavior of the sample proportion ˆp using a normal distribution,
the sample mean ¯x can also be modeled using a normal distribution when certain conditions are
met. However, we’ll soon learn that a new distribution, called the t-distribution, tends to be more
useful when working with the sample mean. We’ll ﬁrst learn about this new distribution, then we’ll
use it to construct conﬁdence intervals and conduct hypothesis tests for the mean.


7.1.1  The sampling distribution of  ¯x¯x¯x

    The sample mean tends to follow a normal distribution centered at the population mean, µ,
when certain conditions are met.  Additionally, we can compute a standard error for the sample
mean using the population standard deviation σ and the sample size n.


  CENTRAL LIMIT THEOREM FOR THE SAMPLE MEAN
  When we collect a suﬃciently large sample of n independent observations from a population
  with mean µ and standard deviation σ, the sampling distribution of ¯x will be nearly normal
  with

                                                          σ
               Mean = µ                Standard Error (SE) = √n


Before diving into conﬁdence intervals and hypothesis tests using ¯x, we ﬁrst need to cover two topics:

   • When we modeled  ˆp using the normal distribution, certain conditions had to be satisﬁed.
    The conditions for working with ¯x are a little more complex, and we’ll spend Section 7.1.2
      discussing how to check conditions for inference.

   • The standard error is dependent on the population standard deviation, σ. However, we rarely
    know σ, and instead we must estimate it. Because this estimation is itself imperfect, we use a
    new distribution called the t-distribution to ﬁx this problem, which we discuss in Section 7.1.3.


7.1.2  Evaluating the two conditions required for modeling  ¯x¯x¯x

Two conditions are required to apply the Central Limit Theorem for a sample mean ¯x:

Independence. The sample observations must be independent, The most common way to satisfy
      this condition is when the sample is a simple random sample from the population.  If the
     data come from a random process, analogous to rolling a die, this would also satisfy the
     independence condition.

Normality. When a sample is small, we also require that the sample observations come from a
     normally distributed population. We can relax this condition more and more for larger and
      larger sample sizes. This condition is obviously vague, making it diﬃcult to evaluate, so next
    we introduce a couple rules of thumb to make checking this condition easier.


  RULES OF THUMB: HOW TO PERFORM THE NORMALITY CHECK
  There is no perfect way to check the normality condition, so instead we use two rules of thumb:

  n < 30:  If the sample size n is less than 30 and there are no clear outliers in the data, then we
        typically assume the data come from a nearly normal distribution to satisfy the condition.

  n ≥30:  If the sample size n is at least 30 and there are no particularly extreme outliers, then
      we typically assume the sampling distribution of ¯x is nearly normal, even if the underlying
        distribution of individual observations is not.

---

# OpenIntro Statistics, 4th edition

## 7.1 — One-sample means with the t-distribution

### PDF page 252

252                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


                   In this ﬁrst course in statistics, you aren’t expected to develop perfect judgement on the nor-
              mality condition. However, you are expected to be able to handle clear cut cases based on the rules
                of thumb.1


          EXAMPLE 7.1
              Consider the following two plots that come from simple random samples from diﬀerent populations.
              Their sample sizes are n1 = 15 and n2 = 50.

                           4                                           25
                                                                        20                           3
                                                                        15
                           2
                                                                        10                                                                                    Frequency                                                                                                                                                          Frequency
                           1                                                                         5
                           0                                            0
                              0        2        4        6                   0             10            20
                                Sample 1 Observations (n = 15)                    Sample 2 Observations (n = 50)

            Are the independence and normality conditions met in each case?

            Each samples is from a simple random sample of its respective population, so the independence
              condition is satisﬁed. Let’s next check the normality condition for each using the rule of thumb.

           The ﬁrst sample has fewer than 30 observations, so we are watching for any clear outliers. None are
               present; while there is a small gap in the histogram on the right, this gap is small and 20% of the
              observations in this small sample are represented in that far right bar of the histogram, so we can
              hardly call these clear outliers. With no clear outliers, the normality condition is reasonably met.

           The second sample has a sample size greater than 30 and includes an outlier that appears to be
              roughly 5 times further from the center of the distribution than the next furthest observation. This
                   is an example of a particularly extreme outlier, so the normality condition would not be satisﬁed.


                   In practice, it’s typical to also do a mental check to evaluate whether we have reason to believe
              the underlying population would have moderate skew (if n < 30) or have particularly extreme outliers
             (n ≥30) beyond what we observe in the data. For example, consider the number of followers for each
               individual account on Twitter, and then imagine this distribution. The large majority of accounts
             have built up a couple thousand followers or fewer, while a relatively tiny fraction have amassed
               tens of millions of followers, meaning the distribution is extremely skewed. When we know the data
            come from such an extremely skewed distribution, it takes some eﬀort to understand what sample
                 size is large enough for the normality condition to be satisﬁed.


            7.1.3  Introducing the t-distribution

                   In practice, we cannot directly calculate the standard error for ¯x since we do not know the
              population standard deviation, σ. We encountered a similar issue when computing the standard
               error for a sample proportion, which relied on the population proportion, p. Our solution in the
              proportion context was to use sample value in place of the population value when computing the
              standard error. We’ll employ a similar strategy for computing the standard error of ¯x, using the
             sample standard deviation s in place of σ:

                                                 σ     s
                                   SE = √n ≈ √n

             This strategy tends to work well when we have a lot of data and can estimate σ using s accurately.
             However, the estimate is less precise with smaller samples, and this leads to problems when using
              the normal distribution to model ¯x.

                 1More nuanced guidelines would consider further relaxing the particularly extreme outlier check when the sample
                    size is very large. However, we’ll leave further discussion here to a future course.

---

# OpenIntro Statistics, 4th edition

## 7.1 — One-sample means with the t-distribution

### PDF page 253

7.1. ONE-SAMPLE MEANS WITH THE T-DISTRIBUTION                                         253


     We’ll ﬁnd it useful to use a new distribution for inference calculations called the t-distribution.
A t-distribution, shown as a solid line in Figure 7.1, has a bell shape. However, its tails are thicker
than the normal distribution’s, meaning observations are more likely to fall beyond two standard deviations from the mean than under the normal distribution. The extra thick tails of the t-distribution
are exactly the correction needed to resolve the problem of using s in place of σ in the SE calculation.


                                                     Normal
                                                                      t−distribution





                   −4       −2        0        2        4

              Figure 7.1: Comparison of a t-distribution and a normal distribution.


    The t-distribution is always centered at zero and has a single parameter: degrees of freedom.
The degrees of freedom (dfdfdf) describes the precise form of the bell-shaped t-distribution. Several
t-distributions are shown in Figure 7.2 in comparison to the normal distribution.
     In general, we’ll use a t-distribution with df = n−1 to model the sample mean when the sample
size is n. That is, when we have more observations, the degrees of freedom will be larger and the
t-distribution will look more like the standard normal distribution; when the degrees of freedom is
about 30 or more, the t-distribution is nearly indistinguishable from the normal distribution.


                                                                    normal
                                                                                                                              t, df = 8
                                                                                                                              t, df = 4
                                                                                                                              t, df = 2
                                                                                                                              t, df = 1




                   −4         −2          0          2          4

        Figure 7.2: The larger the degrees of freedom, the more closely the t-distribution
        resembles the standard normal distribution.




  DEGREES OF FREEDOM (dfdfdf)
  The degrees of freedom describes the shape of the t-distribution. The larger the degrees of
  freedom, the more closely the distribution approximates the normal model.

  When modeling ¯x using the t-distribution, use df = n −1.


    The t-distribution allows us greater ﬂexibility than the normal distribution when analyzing
numerical data.  In practice, it’s common to use statistical software, such as R, Python, or SAS
for these analyses.  Alternatively, a graphing calculator or a t-table may be used; the t-table is
similar to the normal distribution table, and it may be found in Appendix C.2, which includes
usage instructions and examples for those who wish to use this option. No matter the approach you
choose, apply your method using the examples below to conﬁrm your working understanding of the
t-distribution.

---

# OpenIntro Statistics, 4th edition

## 7.1 — One-sample means with the t-distribution

### PDF page 254

254                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA





                                               −4       −2       0        2        4

                      Figure 7.3: The t-distribution with 18 degrees of freedom. The area below -2.10
                     has been shaded.





                               −4     −2      0      2      4       −4    −2     0      2      4

                      Figure 7.4:  Left: The t-distribution with 20 degrees of freedom, with the area
                     above 1.65 shaded. Right: The t-distribution with 2 degrees of freedom, with the
                      area further than 3 units from 0 shaded.



          EXAMPLE 7.2
           What proportion of the t-distribution with 18 degrees of freedom falls below -2.10?

              Just like a normal probability problem, we ﬁrst draw the picture in Figure 7.3 and shade the area
             below -2.10. Using statistical software, we can obtain a precise value: 0.0250.




          EXAMPLE 7.3
         A t-distribution with 20 degrees of freedom is shown in the left panel of Figure 7.4. Estimate the
              proportion of the distribution falling above 1.65.

            With a normal distribution, this would correspond to about 0.05, so we should expect the t-
               distribution to give us a value in this neighborhood. Using statistical software: 0.0573.




          EXAMPLE 7.4
         A t-distribution with 2 degrees of freedom is shown in the right panel of Figure 7.4. Estimate the
              proportion of the distribution falling more than 3 units from the mean (above or below).

            With so few degrees of freedom, the t-distribution will give a more notably diﬀerent value than the
             normal distribution. Under a normal distribution, the area would be about 0.003 using the 68-95-
               99.7 rule. For a t-distribution with df = 2, the area in both tails beyond 3 units totals 0.0955. This
              area is dramatically diﬀerent than what we obtain from the normal distribution.


           GUIDED PRACTICE 7.5
           What proportion of the t-distribution with 19 degrees of freedom falls above -1.79 units? Use your
               preferred method for ﬁnding tail areas.2





               2We want to ﬁnd the shaded area above -1.79 (we leave the picture to you). The lower tail area has an area of
                  0.0447, so the upper area would have an area of 1 −0.0447 = 0.9553.

---

# OpenIntro Statistics, 4th edition

## 7.1 — One-sample means with the t-distribution

### PDF page 255

7.1. ONE-SAMPLE MEANS WITH THE T-DISTRIBUTION                                         255


7.1.4  One sample t-conﬁdence intervals

     Let’s get our ﬁrst taste of applying the t-distribution in the context of an example about the
mercury content of dolphin muscle. Elevated mercury concentrations are an important problem for
both dolphins and other animals, like humans, who occasionally eat them.





                    Figure 7.5: A Risso’s dolphin.
          —————————–
                     Photo by Mike Baird (www.bairdphotos.com). CC BY 2.0 license.


   We will identify a conﬁdence interval for the average mercury content in dolphin muscle using a
sample of 19 Risso’s dolphins from the Taiji area in Japan. The data are summarized in Figure 7.6.
The minimum and maximum observed values can be used to evaluate whether or not there are clear
outliers.

                      n      ¯x    s   minimum  maximum
                           19   4.4   2.3      1.7          9.2

        Figure 7.6: Summary of mercury content in the muscle of 19 Risso’s dolphins from
        the Taiji area. Measurements are in micrograms of mercury per wet gram of muscle
        (µg/wet g).



EXAMPLE 7.6
Are the independence and normality conditions satisﬁed for this data set?

The observations are a simple random sample, therefore independence is reasonable. The summary
statistics in Figure 7.6 do not suggest any clear outliers, since all observations are within 2.5 standard
deviations of the mean. Based on this evidence, the normality condition seems reasonable.

     In the normal model, we used z⋆and the standard error to determine the width of a conﬁdence
interval. We revise the conﬁdence interval formula slightly when using the t-distribution:

                                                                              s
             point estimate ± t⋆df × SE      →                     ¯x ± t⋆df × √n


EXAMPLE 7.7
Using the summary statistics in Figure 7.6, compute the standard error for the average mercury
content in the n = 19 dolphins.

                              √We plug in s and n into the formula: SE = s/√n = 2.3/  19 = 0.528.

---

# OpenIntro Statistics, 4th edition

## 7.1 — One-sample means with the t-distribution

### PDF page 256

256                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


               The value t⋆df is a cutoﬀwe obtain based on the conﬁdence level and the t-distribution with df
              degrees of freedom. That cutoﬀis found in the same way as with a normal distribution: we ﬁnd
                 t⋆df such that the fraction of the t-distribution with df degrees of freedom within a distance t⋆df of 0
             matches the conﬁdence level of interest.


          EXAMPLE 7.8
          When n = 19, what is the appropriate degrees of freedom? Find t⋆df for this degrees of freedom and
              the conﬁdence level of 95%

           The degrees of freedom is easy to calculate: df = n −1 = 18.
             Using statistical software, we ﬁnd the cutoﬀwhere the upper tail is equal to 2.5%: t⋆18 = 2.10. The
              area below -2.10 will also be equal to 2.5%. That is, 95% of the t-distribution with df = 18 lies
              within 2.10 units of 0.


          EXAMPLE 7.9
           Compute and interpret the 95% conﬁdence interval for the average mercury content in Risso’s
               dolphins.

         We can construct the conﬁdence interval as

                                                    ¯x ± t⋆18 × SE →   4.4 ± 2.10 × 0.528 →   (3.29, 5.51)

         We are 95% conﬁdent the average mercury content of muscles in Risso’s dolphins is between 3.29
            and 5.51 µg/wet gram, which is considered extremely high.




              FINDING A t-CONFIDENCE INTERVAL FOR THE MEAN
              Based on a sample of n independent and nearly normal observations, a conﬁdence interval for
                the population mean is

                                                                                          s
                            point estimate ± t⋆df × SE      →                   ¯x ± t⋆df × √n

               where ¯x is the sample mean, t⋆df corresponds to the conﬁdence level and degrees of freedom df,
              and SE is the standard error as estimated by the sample.



           GUIDED PRACTICE 7.10
            The FDA’s webpage provides some data on mercury content of ﬁsh. Based on a sample of 15 croaker
              white ﬁsh (Paciﬁc), a sample mean and standard deviation were computed as 0.287 and 0.069 ppm
               (parts per million), respectively. The 15 observations ranged from 0.18 to 0.41 ppm. We will assume
               these observations are independent. Based on the summary statistics of the data, do you have any
               objections to the normality condition of the individual observations?3




          EXAMPLE 7.11
             Estimate the standard error of ¯x = 0.287 ppm using the data summaries in Guided Practice 7.10.
                   If we are to use the t-distribution to create a 90% conﬁdence interval for the actual mean of the
             mercury content, identify the degrees of freedom and t⋆df.

           The standard error: SE = 0.069√  = 0.0178.
                                                15
             Degrees of freedom: df = n −1 = 14.
              Since the goal is a 90% conﬁdence interval, we choose t⋆14 so that the two-tail area is 0.1: t⋆14 = 1.76.

                 3The sample size is under 30, so we check for obvious outliers:  since all observations are within 2 standard
                 deviations of the mean, there are no such clear outliers.

---

# OpenIntro Statistics, 4th edition

## 7.1 — One-sample means with the t-distribution

### PDF page 257

7.1. ONE-SAMPLE MEANS WITH THE T-DISTRIBUTION                                         257



  CONFIDENCE INTERVAL FOR A SINGLE MEAN
  Once you’ve determined a one-mean conﬁdence interval would be helpful for an application,
  there are four steps to constructing the interval:

  Prepare. Identify ¯x, s, n, and determine what conﬁdence level you wish to use.

  Check. Verify the conditions to ensure ¯x is nearly normal.

  Calculate.  If the conditions hold, compute SE, ﬁnd t⋆df, and construct the interval.

  Conclude. Interpret the conﬁdence interval in the context of the problem.



GUIDED PRACTICE 7.12
Using the information and results of Guided Practice 7.10 and Example 7.11, compute a 90% conﬁdence interval for the average mercury content of croaker white ﬁsh (Paciﬁc).4




GUIDED PRACTICE 7.13
The 90% conﬁdence interval from Guided Practice 7.12 is 0.256 ppm to 0.318 ppm. Can we say that
90% of croaker white ﬁsh (Paciﬁc) have mercury levels between 0.256 and 0.318 ppm?5




7.1.5  One sample t-tests

Is the typical US runner getting faster or slower over time? We consider this question in the context
of the Cherry Blossom Race, which is a 10-mile race in Washington, DC each spring.
    The average time for all runners who ﬁnished the Cherry Blossom Race in 2006 was 93.29
minutes (93 minutes and about 17 seconds). We want to determine using data from 100 participants
in the 2017 Cherry Blossom Race whether runners in this race are getting faster or slower, versus
the other possibility that there has been no change.


GUIDED PRACTICE 7.14
What are appropriate hypotheses for this context?6




GUIDED PRACTICE 7.15
The data come from a simple random sample of all participants, so the observations are independent.
However, should we be worried about the normality condition? See Figure 7.7 for a histogram of
the diﬀerences and evaluate if we can move forward.7

   When completing a hypothesis test for the one-sample mean, the process is nearly identical to
completing a hypothesis test for a single proportion. First, we ﬁnd the Z-score using the observed
value, null value, and standard error; however, we call it a T-score since we use a t-distribution for
calculating the tail area. Then we ﬁnd the p-value using the same ideas we used previously: ﬁnd
the one-tail area under the sampling distribution, and double it.



    4 ¯x ± t⋆14 × SE →0.287 ± 1.76 × 0.0178 →(0.256, 0.318). We are 90% conﬁdent that the average mercury
content of croaker white ﬁsh (Paciﬁc) is between 0.256 and 0.318 ppm.
    5 No, a conﬁdence interval only provides a range of plausible values for a population parameter, in this case the
population mean. It does not describe what we might observe for individual observations.
   6H0: The average 10-mile run time was the same for 2006 and 2017. µ = 93.29 minutes. HA: The average 10-mile
run time for 2017 was diﬀerent than that of 2006. µ̸ = 93.29 minutes.
   7With a sample of 100, we should only be concerned if there is are particularly extreme outliers. The histogram
of the data doesn’t show any outliers of concern (and arguably, no outliers at all).

---

# OpenIntro Statistics, 4th edition

## 7.1 — One-sample means with the t-distribution

### PDF page 258

258                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


                               20

                               15

                               10                                                                                                    Frequency
                                5

                                0
                                        60       80       100      120      140
                                                   Time (Minutes)

                         Figure 7.7: A histogram of time for the sample Cherry Blossom Race data.



          EXAMPLE 7.16
            With both the independence and normality conditions satisﬁed, we can proceed with a hypothesis
                test using the t-distribution. The sample mean and sample standard deviation of the sample of 100
              runners from the 2017 Cherry Blossom Race are 97.32 and 16.98 minutes, respectively. Recall that
              the sample size is 100 and the average run time in 2006 was 93.29 minutes. Find the test statistic
            and p-value. What is your conclusion?

           To ﬁnd the test statistic (T-score), we ﬁrst must determine the standard error:
                                  √
                                SE = 16.98/  100 = 1.70

          Now we can compute the T-score using the sample mean (97.32), null value (93.29), and SE:

                                                      97.32 −93.29
                                       T =        = 2.37
                                                            1.70

             For df = 100 −1 = 99, we can determine using statistical software (or a t-table) that the one-tail
              area is 0.01, which we double to get the p-value: 0.02.

             Because the p-value is smaller than 0.05, we reject the null hypothesis. That is, the data provide
              strong evidence that the average run time for the Cherry Blossom Run in 2017 is diﬀerent than
              the 2006 average. Since the observed value is above the null value and we have rejected the null
               hypothesis, we would conclude that runners in the race were slower on average in 2017 than in 2006.



             HYPOTHESIS TESTING FOR A SINGLE MEAN
              Once you’ve determined a one-mean hypothesis test is the correct procedure, there are four
                 steps to completing the test:

              Prepare. Identify the parameter of interest, list out hypotheses, identify the signiﬁcance level,
                   and identify ¯x, s, and n.

             Check. Verify conditions to ensure ¯x is nearly normal.

               Calculate.  If the conditions hold, compute SE, compute the T-score, and identify the p-value.

              Conclude. Evaluate the hypothesis test by comparing the p-value to α, and provide a conclu-
                       sion in the context of the problem.

---

# OpenIntro Statistics, 4th edition

## 7.1 — One-sample means with the t-distribution

### PDF page 259

7.1. ONE-SAMPLE MEANS WITH THE T-DISTRIBUTION                                         259


Exercises


7.1   Identify the critical t. An independent random sample is selected from an approximately normal
population with unknown standard deviation. Find the degrees of freedom and the critical t-value (t⋆) for
the given sample size and conﬁdence level.

(a) n = 6, CL = 90%
(b) n = 21, CL = 98%
(c) n = 29, CL = 95%
(d) n = 12, CL = 99%

7.2   t-distribution. The ﬁgure on the right shows three unimodal and symmetric curves: the standard
normal (z) distribution, the t-distribution with 5 degrees of freedom, and the t-distribution with 1 degree of
freedom. Determine which is which, and explain your reasoning.

                                                                                                    solid
                                                                           dashed
                                                                                         dotted





                                    −4        −2         0         2         4


7.3  Find the p-value, Part I. An independent random sample is selected from an approximately normal
population with an unknown standard deviation. Find the p-value for the given sample size and test statistic.
Also determine if the null hypothesis would be rejected at α = 0.05.

(a) n = 11, T = 1.91
(b) n = 17, T = −3.45
(c) n = 7, T = 0.83
(d) n = 28, T = 2.13

7.4  Find the p-value, Part II. An independent random sample is selected from an approximately normal
population with an unknown standard deviation. Find the p-value for the given sample size and test statistic.
Also determine if the null hypothesis would be rejected at α = 0.01.

(a) n = 26, T = 2.485
(b) n = 18, T = 0.5

7.5  Working backwards, Part I. A 95% conﬁdence interval for a population mean, µ, is given as (18.985,
21.015). This conﬁdence interval is based on a simple random sample of 36 observations.  Calculate the
sample mean and standard deviation. Assume that all conditions necessary for inference are satisﬁed. Use
the t-distribution in any calculations.

7.6  Working backwards, Part  II. A 90% conﬁdence interval for a population mean is (65, 77).  The
population distribution is approximately normal and the population standard deviation is unknown. This
conﬁdence interval is based on a simple random sample of 25 observations. Calculate the sample mean, the
margin of error, and the sample standard deviation.

---

# OpenIntro Statistics, 4th edition

## 7.1 — One-sample means with the t-distribution

### PDF page 260

260                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


                7.7  Sleep habits of New Yorkers. New York is known as “the city that never sleeps”. A random sample
                 of 25 New Yorkers were asked how much sleep they get per night. Statistical summaries of these data are
             shown below. The point estimate suggests New Yorkers sleep less than 8 hours a night on average. Is the
                 result statistically signiﬁcant?

                                            n         ¯x       s   min  max
                                                25   7.73   0.77   6.17   9.78

                (a) Write the hypotheses in symbols and in words.
                (b) Check conditions, then calculate the test statistic, T, and the associated degrees of freedom.
                 (c) Find and interpret the p-value in this context. Drawing a picture may be helpful.
                (d) What is the conclusion of the hypothesis test?
                 (e)  If you were to construct a 90% conﬁdence interval that corresponded to this hypothesis test, would you
                   expect 8 hours to be in the interval?

                7.8  Heights of adults. Researchers studying anthropometry collected body girth measurements and skele-
                  tal diameter measurements, as well as age, weight, height and gender, for 507 physically active individuals.
            The histogram below shows the sample distribution of heights in centimeters.8
              100

               80

               60                                                             Min      147.2
                                                                      Q1       163.8
               40                                                                 Median   170.3
                                                                          Mean     171.1
               20                                                      SD          9.4
                                                                      Q3       177.8
                0                                                       Max      198.1
                        150       160       170       180       190       200
                                  Height

                (a) What is the point estimate for the average height of active individuals? What about the median?
                (b) What is the point estimate for the standard deviation of the heights of active individuals? What about
                   the IQR?
                 (c) Is a person who is 1m 80cm (180 cm) tall considered unusually tall? And is a person who is 1m 55cm
                 (155cm) considered unusually short? Explain your reasoning.
                (d) The researchers take another random sample of physically active individuals. Would you expect the mean
                and the standard deviation of this new sample to be the ones given above? Explain your reasoning.
                 (e) The sample means obtained are point estimates for the mean height of all active individuals,  if the
                  sample of individuals is equivalent to a simple random sample. What measure do we use to quantify the
                      variability of such an estimate? Compute this quantity using the data from the original sample under
                   the condition that the data are a simple random sample.

                7.9  Find the mean. You are given the following hypotheses:

                                              H0 : µ = 60
                                       HA : µ̸ = 60

          We know that the sample standard deviation is 8 and the sample size is 20. For what sample mean would
               the p-value be equal to 0.05? Assume that all conditions necessary for inference are satisﬁed.





                  8G. Heinz et al. “Exploring relationships in body dimensions”. In: Journal of Statistics Education 11.2 (2003).

---

# OpenIntro Statistics, 4th edition

## 7.1 — One-sample means with the t-distribution

### PDF page 261

7.1. ONE-SAMPLE MEANS WITH THE T-DISTRIBUTION                                         261


7.10  t⋆vs. z⋆. For a given conﬁdence level, t⋆df  is larger than z⋆. Explain how t∗df being slightly larger
than z∗aﬀects the width of the conﬁdence interval.

7.11  Play the piano. Georgianna claims that in a small city renowned for its music school, the average
child takes less than 5 years of piano lessons. We have a random sample of 20 children from the city, with a
mean of 4.6 years of piano lessons and a standard deviation of 2.2 years.

(a) Evaluate Georgianna’s claim (or that the opposite might be true) using a hypothesis test.
(b) Construct a 95% conﬁdence interval for the number of years students in this city take piano lessons, and
    interpret it in context of the data.
(c) Do your results from the hypothesis test and the conﬁdence interval agree? Explain your reasoning.

7.12  Auto exhaust and lead exposure. Researchers interested in lead exposure due to car exhaust sampled
the blood of 52 police oﬃcers subjected to constant inhalation of automobile exhaust fumes while working
traﬃc enforcement in a primarily urban environment. The blood samples of these oﬃcers had an average
lead concentration of 124.32 µg/l and a SD of 37.74 µg/l; a previous study of individuals from a nearby
suburb, with no history of exposure, found an average blood level concentration of 35 µg/l.9

(a) Write down the hypotheses that would be appropriate for testing if the police oﬃcers appear to have
    been exposed to a diﬀerent concentration of lead.
(b) Explicitly state and check all conditions necessary for inference on these data.
(c) Regardless of your answers in part (b), test the hypothesis that the downtown police oﬃcers have a
    higher lead exposure than the group in the previous study. Interpret your results in context.

7.13  Car insurance savings. A market researcher wants to evaluate car insurance savings at a competing
company. Based on past studies he is assuming that the standard deviation of savings is $100. He wants
to collect data such that he can get a margin of error of no more than $10 at a 95% conﬁdence level. How
large of a sample should he collect?

7.14  SAT scores. The standard deviation of SAT scores for students at a particular Ivy League college is
250 points. Two statistics students, Raina and Luke, want to estimate the average SAT score of students at
this college as part of a class project. They want their margin of error to be no more than 25 points.

(a) Raina wants to use a 90% conﬁdence interval. How large a sample should she collect?
(b) Luke wants to use a 99% conﬁdence interval. Without calculating the actual sample size, determine
    whether his sample should be larger or smaller than Raina’s, and explain your reasoning.
(c) Calculate the minimum required sample size for Luke.





   9WI Mortada et al. “Study of lead exposure from automobile exhaust as a risk for nephrotoxicity among traﬃc
policemen.” In: American journal of nephrology 21.4 (2000), pp. 274–279.

---

# OpenIntro Statistics, 4th edition

## 7.2 — Paired data

### PDF page 262

262                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


        7.2  Paired data



              In an earlier edition of this textbook, we found that Amazon prices were, on average, lower than
              those of the UCLA Bookstore for UCLA courses in 2010. It’s been several years, and many stores
             have adapted to the online market, so we wondered, how is the UCLA Bookstore doing today?
            We sampled 201 UCLA courses.  Of those, 68 required books could be found on Amazon.
         A portion of the data set from these courses is shown in Figure 7.8, where prices are in US dollars.

                         subject                    course number   bookstore  amazon   price diﬀerence
                   1  American Indian Studies  M10               47.97      47.45         0.52
                   2  Anthropology            2                  14.26      13.55         0.71
                   3  Arts and Architecture     10                 13.50      12.53         0.97
                                                                                                        ...             ...                                                                                                                               ...                                                                                                     ...                                                   ...                                                                ...
                  68  Jewish Studies         M10               35.96      32.40         3.56

                                     Figure 7.8: Four cases of the textbooks data set.



            7.2.1  Paired observations

                Each textbook has two corresponding prices in the data set: one for the UCLA Bookstore and
             one for Amazon. When two sets of observations have this special correspondence, they are said to
             be paired.


              PAIRED DATA
            Two sets of observations are paired  if each observation in one set has a special correspondence
                 or connection with exactly one observation in the other data set.


               To analyze paired data, it is often useful to look at the diﬀerence in outcomes of each pair of
               observations. In the textbook data, we look at the diﬀerences in prices, which is represented as the
            price difference variable in the data set. Here the diﬀerences are taken as

                           UCLA Bookstore price −Amazon price

                 It is important that we always subtract using a consistent order; here Amazon prices are always
              subtracted from UCLA prices. The ﬁrst diﬀerence shown in Figure 7.8 is computed as 47.97 −
              47.45 = 0.52. Similarly, the second diﬀerence is computed as 14.26 −13.55 = 0.71, and the third
                   is 13.50 −12.53 = 0.97. A histogram of the diﬀerences is shown in Figure 7.9. Using diﬀerences
             between paired observations is a common and useful way to analyze paired data.


                                 30

                                 20
                                                                                                         Frequency  10

                                  0
                                   −$20     $0      $20     $40     $60     $80
                                  UCLA Bookstore Price − Amazon Price (USD)

                           Figure 7.9: Histogram of the diﬀerence in price for each book sampled.

---

# OpenIntro Statistics, 4th edition

## 7.2 — Paired data

### PDF page 263

7.2. PAIRED DATA                                                                              263


7.2.2  Inference for paired data

    To analyze a paired data set, we simply analyze the diﬀerences. We can use the same tdistribution techniques we applied in Section 7.1.

                                             ndiﬀ         ¯xdiﬀ         sdiﬀ
                                  68      3.58     13.42

                  Figure 7.10: Summary statistics for the 68 price diﬀerences.



EXAMPLE 7.17
Set up a hypothesis test to determine whether, on average, there is a diﬀerence between Amazon’s
price for a book and the UCLA bookstore’s price. Also, check the conditions for whether we can
move forward with the test using the t-distribution.

We are considering two scenarios: there is no diﬀerence or there is some diﬀerence in average prices.

 H0: µdiﬀ= 0. There is no diﬀerence in the average textbook price.
HA: µdiﬀ̸ = 0. There is a diﬀerence in average prices.

Next, we check the independence and normality conditions. The observations are based on a simple
random sample, so independence is reasonable. While there are some outliers, n = 68 and none
of the outliers are particularly extreme, so the normality of ¯x is satisﬁed. With these conditions
satisﬁed, we can move forward with the t-distribution.


EXAMPLE 7.18
Complete the hypothesis test started in Example 7.17.

To compute the test compute the standard error associated with ¯xdiﬀusing the standard deviation
of the diﬀerences (sdiﬀ= 13.42) and the number of diﬀerences (ndiﬀ= 68):

                                               sdiﬀ     13.42
                             SE¯xdiﬀ= √ndiﬀ = √ 68 = 1.63

The test statistic is the T-score of ¯xdiﬀunder the null condition that the actual mean diﬀerence is 0:

                                ¯xdiﬀ−0    3.58 −0
                         T =      =      = 2.20
                                            SE¯xdiﬀ       1.63

To visualize the p-value, the sampling distribution of ¯xdiﬀis drawn as though H0 is true, and the
p-value is represented by the two shaded tails:





                                                µ0 = 0              xdiff = 2.98


The degrees of freedom is df = 68 −1 = 67. Using statistical software, we ﬁnd the one-tail area of
0.0156. Doubling this area gives the p-value: 0.0312.

Because the p-value is less than 0.05, we reject the null hypothesis. Amazon prices are, on average,
lower than the UCLA Bookstore prices for UCLA courses.

---

# OpenIntro Statistics, 4th edition

## 7.2 — Paired data

### PDF page 264

264                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA



           GUIDED PRACTICE 7.19
             Create a 95% conﬁdence interval for the average price diﬀerence between books at the UCLA book-
               store and books on Amazon.10



           GUIDED PRACTICE 7.20
         We have strong evidence that Amazon is, on average, less expensive. How should this conclusion
              aﬀect UCLA student buying habits? Should UCLA students always buy their books on Amazon?11





                   10Conditions have already veriﬁed and the standard error computed in Example 7.17. To ﬁnd the interval, identify
                   t⋆67 using statistical software or the t-table (t⋆67 = 2.00), and plug it, the point estimate, and the standard error into
                 the conﬁdence interval formula:

                                     point estimate ± z⋆× SE →   3.58 ± 2.00 × 1.63 →   (0.32, 6.84)

           We are 95% conﬁdent that Amazon is, on average, between $0.32 and $6.84 less expensive than the UCLA Bookstore
                   for UCLA course books.
                 11The average price diﬀerence is only mildly useful for this question. Examine the distribution shown in Figure 7.9.
               There are certainly a handful of cases where Amazon prices are far below the UCLA Bookstore’s, which suggests it
                       is worth checking Amazon (and probably other online sites) before purchasing. However, in many cases the Amazon
                  price is above what the UCLA Bookstore charges, and most of the time the price isn’t that diﬀerent. Ultimately, if
                  getting a book immediately from the bookstore is notably more convenient, e.g. to get started on reading or homework,
                       it’s likely a good idea to go with the UCLA Bookstore unless the price diﬀerence on a speciﬁc book happens to be
                 quite large.
                  For reference, this is a very diﬀerent result from what we (the authors) had seen in a similar data set from 2010. At
                 that time, Amazon prices were almost uniformly lower than those of the UCLA Bookstore’s and by a large margin,
              making the case to use Amazon over the UCLA Bookstore quite compelling at that time. Now we frequently check
                 multiple websites to ﬁnd the best price.

---

# OpenIntro Statistics, 4th edition

## 7.2 — Paired data

### PDF page 265

7.2. PAIRED DATA                                                                              265


Exercises


7.15  Air quality. Air quality measurements were collected in a random sample of 25 country capitals in
2013, and then again in the same cities in 2014. We would like to use these data to compare average air
quality between the two years. Should we use a paired or non-paired test? Explain your reasoning.

7.16  True / False: paired. Determine if the following statements are true or false. If false, explain.

(a) In a paired analysis we ﬁrst take the diﬀerence of each pair of observations, and then we do inference
    on these diﬀerences.
(b) Two data sets of diﬀerent sizes cannot be analyzed as paired data.
(c) Consider two sets of data that are paired with each other. Each observation in one data set has a natural
    correspondence with exactly one observation from the other data set.
(d) Consider two sets of data that are paired with each other. Each observation in one data set is subtracted
    from the average of the other data set’s observations.

7.17  Paired or not? Part I. In each of the following scenarios, determine if the data are paired.

(a) Compare pre- (beginning of semester) and post-test (end of semester) scores of students.
(b) Assess gender-related salary gap by comparing salaries of randomly sampled men and women.
(c) Compare artery thicknesses at the beginning of a study and after 2 years of taking Vitamin E for the
   same group of patients.
(d) Assess eﬀectiveness of a diet regimen by comparing the before and after weights of subjects.

7.18  Paired or not? Part II. In each of the following scenarios, determine if the data are paired.

(a) We would like to know if Intel’s stock and Southwest Airlines’ stock have similar rates of return. To ﬁnd
    out, we take a random sample of 50 days, and record Intel’s and Southwest’s stock on those same days.
(b) We randomly sample 50 items from Target stores and note the price for each. Then we visit Walmart
   and collect the price for each of those same 50 items.
(c) A school board would like to determine whether there is a diﬀerence in average SAT scores for students
    at one high school versus another high school in the district. To check, they take a simple random
    sample of 100 students from each high school.

7.19  Global warming, Part I. Let’s consider a limited set of climate data, examining temperature diﬀerences
in 1948 vs 2018. We sampled 197 locations from the National Oceanic and Atmospheric Administration’s
(NOAA) historical data, where the data was available for both years of interest. We want to know: were
there more days with temperatures exceeding 90°F in 2018 or in 1948?12 The diﬀerence in number of days
exceeding 90°F (number of days in 2018 - number of days in 1948) was calculated for each of the 197 locations.
The average of these diﬀerences was 2.9 days with a standard deviation of 17.2 days. We are interested in
determining whether these data provide strong evidence that there were more days in 2018 that exceeded
90°F from NOAA’s weather stations.

(a) Is there a relationship between the observations collected in 1948
   and 2018? Or are the observations in the two groups independent?
    Explain.
(b) Write hypotheses for this research in symbols and in words.
                                                                                             50(c) Check the conditions required to complete this test. A histogram
     of the diﬀerences is given to the right.                                        40
                                                                                             30(d) Calculate the test statistic and ﬁnd the p-value.
                                                                                             20
(e) Use α = 0.05 to evaluate the test, and interpret your conclusion
                                                                                             10    in context.
                                                                                              0
(f) What type of error might we have made? Explain in context what
                                                                                                 −60−60  −40−40  −20−20   00    2020   4040   6060
    the error means.
(g) Based on the results of this hypothesis test, would you expect a                  Differences in Number of Days
    conﬁdence interval for the average diﬀerence between the number
     of days exceeding 90°F from 1948 and 2018 to include 0? Explain
    your reasoning.




  12NOAA, www.ncdc.noaa.gov/cdo-web/datasets, April 24, 2019.

---

# OpenIntro Statistics, 4th edition

## 7.2 — Paired data

### PDF page 266

266                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


               7.20  High School and Beyond, Part I. The National Center of Education Statistics conducted a survey of
               high school seniors, collecting test data on reading, writing, and several other subjects. Here we examine a
               simple random sample of 200 students from this survey. Side-by-side box plots of reading and writing scores
                as well as a histogram of the diﬀerences in scores are shown below.

                                                     40
                   80
                                                     30
                   60
                                     scores                                      20
                   40                                  10

                                                      0                   20
                                                            −20     −10      0      10      20                                 read                 write
                                                                              Differences in scores (read − write)

                (a) Is there a clear diﬀerence in the average reading and writing scores?
                (b) Are the reading and writing scores of each student independent of each other?
                 (c) Create hypotheses appropriate for the following research question: is there an evident diﬀerence in the
                   average scores of students in the reading and writing exam?
                (d) Check the conditions required to complete this test.
                 (e) The average observed diﬀerence in scores is ¯xread−write = −0.545, and the standard deviation of the
                    diﬀerences is 8.887 points. Do these data provide convincing evidence of a diﬀerence between the average
                     scores on the two exams?
                  (f) What type of error might we have made? Explain what the error means in the context of the application.
                (g) Based on the results of this hypothesis test, would you expect a conﬁdence interval for the average
                   diﬀerence between the reading and writing scores to include 0? Explain your reasoning.

               7.21  Global warming, Part II. We considered the change in the number of days exceeding 90°F from 1948
             and 2018 at 197 randomly sampled locations from the NOAA database in Exercise 7.19. The mean and
               standard deviation of the reported diﬀerences are 2.9 days and 17.2 days.

                (a) Calculate a 90% conﬁdence interval for the average diﬀerence between number of days exceeding 90°F
                  between 1948 and 2018. We’ve already checked the conditions for you.
                (b) Interpret the interval in context.
                 (c) Does the conﬁdence interval provide convincing evidence that there were more days exceeding 90°F in
                  2018 than in 1948 at NOAA stations? Explain.

               7.22  High school and beyond, Part II. We considered the diﬀerences between the reading and writing
                scores of a random sample of 200 students who took the High School and Beyond Survey in Exercise 7.20.
            The mean and standard deviation of the diﬀerences are ¯xread−write = −0.545 and 8.887 points.

                (a) Calculate a 95% conﬁdence interval for the average diﬀerence between the reading and writing scores of
                         all students.
                (b) Interpret this interval in context.
                 (c) Does the conﬁdence interval provide convincing evidence that there is a real diﬀerence in the average
                    scores? Explain.

---

# OpenIntro Statistics, 4th edition

## 7.3 — Difference of two means

### PDF page 267

7.3. DIFFERENCE OF TWO MEANS                                                              267


7.3  Difference of two means



In this section we consider a diﬀerence in two population means, µ1 −µ2, under the condition that
the data are not paired. Just as with a single sample, we identify conditions to ensure we can use
the t-distribution with a point estimate of the diﬀerence, ¯x1 −¯x2, and a new standard error formula.
Other than these two diﬀerences, the details are almost identical to the one-mean procedures.
   We apply these methods in three contexts: determining whether stem cells can improve heart
function, exploring the relationship between pregnant womens’ smoking habits and birth weights
of newborns, and exploring whether there is statistically signiﬁcant evidence that one variation of
an exam is harder than another variation.  This section is motivated by questions like “Is there
convincing evidence that newborns from mothers who smoke have a diﬀerent average birth weight
than newborns from mothers who don’t smoke?”


7.3.1  Conﬁdence interval for a difference of means

    Does treatment using embryonic stem cells (ESCs) help improve heart function following a
heart attack?  Figure 7.11 contains summary statistics for an experiment to test ESCs in sheep
that had a heart attack. Each of these sheep was randomly assigned to the ESC or control group,
and the change in their hearts’ pumping capacity was measured in the study. Figure 7.12 provides
histograms of the two data sets. A positive value corresponds to increased pumping capacity, which
generally suggests a stronger recovery. Our goal will be to identify a 95% conﬁdence interval for the
eﬀect of ESCs on the change in heart pumping capacity relative to the control group.

                                  n          ¯x     s
                           ESCs    9   3.50   5.17
                                     control   9   -4.33   2.76

               Figure 7.11: Summary statistics of the embryonic stem cell study.

    The point estimate of the diﬀerence in the heart pumping variable is straightforward to ﬁnd:
it is the diﬀerence in the sample means.

                                     ¯xesc −¯xcontrol = 3.50 −(−4.33) = 7.83

For the question of whether we can model this diﬀerence using a t-distribution, we’ll need to check
new conditions. Like the 2-proportion cases, we will require a more robust version of independence
so we are conﬁdent the two groups are also independent. Secondly, we also check for normality in
each group separately, which in practice is a check for outliers.


  USING THE t-DISTRIBUTION FOR A DIFFERENCE IN MEANS
  The t-distribution can be used for inference when working with the standardized diﬀerence of
  two means if

     • Independence, extended. The data are independent within and between the two groups,
         e.g. the data come from independent random samples or from a randomized experiment.

     • Normality. We check the outliers rules of thumb for each group separately.

  The standard error may be computed as

                     s
                                           σ21   σ22                         SE =    +
                                            n1   n2

  The oﬃcial formula for the degrees of freedom is quite complex and is generally computed using
  software, so instead you may use the smaller of n1 −1 and n2 −1 for the degrees of freedom if
  software isn’t readily available.

---

# OpenIntro Statistics, 4th edition

## 7.3 — Difference of two means

### PDF page 268

268                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA



          EXAMPLE 7.21
           Can the t-distribution be used to make inference using the point estimate, ¯xesc −¯xcontrol = 7.83?

                First, we check for independence. Because the sheep were randomized into the groups, independence
              within and between groups is satisﬁed.

              Figure 7.12 does not reveal any clear outliers in either group. (The ESC group does look a bit more
                 variability, but this is not the same as having clear outliers.)

            With both conditions met, we can use the t-distribution to model the diﬀerence of sample means.


                                        Embryonic stem cell transplant
                                3

                                2

                                1

                                0
                                −10%     −5%      0%      5%      10%      15%
                                            Change in heart pumping function

                                                  Control (no treatment)
                                3

                                2

                                1

                                0
                                −10%     −5%      0%      5%      10%      15%
                                            Change in heart pumping function

                        Figure 7.12: Histograms for both the embryonic stem cell and control group.

               As with the one-sample case, we always compute the standard error using sample standard
               deviations rather than population standard deviations:

                    s                                                                   s2esc    s2control  r 5.172   2.762                        SE =     +     =     +    = 1.95
                                                 nesc    ncontrol       9      9

               Generally, we use statistical software to ﬁnd the appropriate degrees of freedom, or if software isn’t
                available, we can use the smaller of n1 −1 and n2 −1 for the degrees of freedom, e.g.  if using a
                t-table to ﬁnd tail areas. For transparency in the Examples and Guided Practice, we’ll use the latter
             approach for ﬁnding df; in the case of the ESC example, this means we’ll use df = 8.

---

# OpenIntro Statistics, 4th edition

## 7.3 — Difference of two means

### PDF page 269

7.3. DIFFERENCE OF TWO MEANS                                                              269



EXAMPLE 7.22
Calculate a 95% conﬁdence interval for the eﬀect of ESCs on the change in heart pumping capacity
of sheep after they’ve suﬀered a heart attack.

We will use the sample diﬀerence and the standard error that we computed earlier calculations:

                          r 5.172   2.762
                     ¯xesc −¯xcontrol = 7.83          SE =     +    = 1.95
                                                        9      9

Using df = 8, we can identify the critical value of t⋆8 = 2.31 for a 95% conﬁdence interval. Finally,
we can enter the values into the conﬁdence interval formula:

            point estimate ± t⋆× SE →   7.83 ± 2.31 × 1.95 →   (3.32, 12.34)

We are 95% conﬁdent that embryonic stem cells improve the heart’s pumping function in sheep that
have suﬀered a heart attack by 3.32% to 12.34%.


As with past statistical inference applications, there is a well-trodden procedure.

Prepare. Retrieve critical contextual information, and if appropriate, set up hypotheses.

Check. Ensure the required conditions are reasonably satisﬁed.

Calculate. Find the standard error, and then construct a conﬁdence interval, or if conducting a
     hypothesis test, ﬁnd a test statistic and p-value.

Conclude. Interpret the results in the context of the application.

The details change a little from one setting to the next, but this general approach remain the same.


7.3.2  Hypothesis tests for the difference of two means

   A data set called ncbirths represents a random sample of 150 cases of mothers and their newborns in North Carolina over a year. Four cases from this data set are represented in Figure 7.13. We
are particularly interested in two variables: weight and smoke. The weight variable represents the
weights of the newborns and the smoke variable describes which mothers smoked during pregnancy.
We would like to know, is there convincing evidence that newborns from mothers who smoke have
a diﬀerent average birth weight than newborns from mothers who don’t smoke? We will use the
North Carolina sample to try to answer this question. The smoking group includes 50 cases and the
nonsmoking group contains 100 cases.

                           fage  mage  weeks   weight   sex     smoke
                    1  NA     13     37     5.00   female  nonsmoker
                    2  NA     14     36     5.88   female  nonsmoker
                    3    19     15     41     8.13  male    smoker
                                                                                                             ...                             ...                                   ...                                     ...                                         ...             ...
                  150    45     50     36     9.25   female  nonsmoker

        Figure 7.13: Four cases from the ncbirths data set. The value “NA”, shown for
        the ﬁrst two entries of the ﬁrst variable, indicates that piece of data is missing.

---

# OpenIntro Statistics, 4th edition

## 7.3 — Difference of two means

### PDF page 270

270                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA



          EXAMPLE 7.23
              Set up appropriate hypotheses to evaluate whether there is a relationship between a mother smoking
            and average birth weight.

           The null hypothesis represents the case of no diﬀerence between the groups.

             H0: There is no diﬀerence in average birth weight for newborns from mothers who did and did not
                  smoke. In statistical notation: µn −µs = 0, where µn represents non-smoking mothers and µs
                     represents mothers who smoked.

           HA: There is some diﬀerence in average newborn weights from mothers who did and did not smoke
                  (µn −µs̸ = 0).


            We check the two conditions necessary to model the diﬀerence in sample means using the
                t-distribution.

                • Because the data come from a simple random sample, the observations are independent, both
                   within and between samples.

                • With both data sets over 30 observations, we inspect the data in Figure 7.14 for any particularly
                  extreme outliers and ﬁnd none.

              Since both conditions are satisﬁed, the diﬀerence in sample means may be modeled using a t-
                distribution.

                        Mothers Who Smoked                    Mothers Who Did Not Smoke





                  0      2      4      6      8      10          0      2      4      6      8      10
                             Newborn Weights (lbs)                              Newborn Weights (lbs)

                      Figure 7.14: The left panel represents birth weights for infants whose mothers
                     smoked. The right panel represents the birth weights for infants whose mothers
                 who did not smoke.



           GUIDED PRACTICE 7.24
           The summary statistics in Figure 7.15 may be useful for this Guided Practice.13

               (a) What is the point estimate of the population diﬀerence, µn −µs?

              (b) Compute the standard error of the point estimate from part (a).



                                                   smoker  nonsmoker
                                    mean           6.78         7.18
                                                           st. dev.         1.43         1.60
                                         samp. size       50         100

                                Figure 7.15: Summary statistics for the ncbirths data set.


                    13(a) The diﬀerence in sample means is an appropriate point estimate: ¯xn −¯xs = 0.40. (b) The standard error of
                 the estimate can be calculated using the standard error formula:

                       s     s     s                                                                 σ2n     σ2s        s2n      s2s      1.602    1.432                             SE =    +  ≈    +  =     +    = 0.26
                                          nn   ns     nn   ns      100     50

---

# OpenIntro Statistics, 4th edition

## 7.3 — Difference of two means

### PDF page 271

7.3. DIFFERENCE OF TWO MEANS                                                              271



EXAMPLE 7.25
Complete the hypothesis test started in Example 7.23 and Guided Practice 7.24. Use a signiﬁcance
level of α = 0.05. For reference, ¯xn −¯xs = 0.40, SE = 0.26, and the sample sizes were nn = 100
and ns = 50.

We can ﬁnd the test statistic for this test using the values from Guided Practice 7.24:

                                            0.40 −0
                             T =      = 1.54
                                              0.26

The p-value is represented by the two shaded tails in the following plot:





                                          µn −µs = 0 obs. diff


We ﬁnd the single tail area using software (or the t-table in Appendix C.2). We’ll use the smaller of
nn −1 = 99 and ns −1 = 49 as the degrees of freedom: df = 49. The one tail area is 0.065; doubling
this value gives the two-tail area and p-value, 0.135.

The p-value is larger than the signiﬁcance value, 0.05, so we do not reject the null hypothesis. There
is insuﬃcient evidence to say there is a diﬀerence in average birth weight of newborns from North
Carolina mothers who did smoke during pregnancy and newborns from North Carolina mothers who
did not smoke during pregnancy.


GUIDED PRACTICE 7.26
We’ve seen much research suggesting smoking is harmful during pregnancy, so how could we fail to
reject the null hypothesis in Example 7.25? 14




GUIDED PRACTICE 7.27
If we made a Type 2 Error and there is a diﬀerence, what could we have done diﬀerently in data
collection to be more likely to detect the diﬀerence?15


     Public service announcement: while we have used this relatively small data set as an example,
larger data sets show that women who smoke tend to have smaller newborns. In fact, some in the
tobacco industry actually had the audacity to tout that as a beneﬁt of smoking:

       It’s true. The babies born from women who smoke are smaller, but they’re just as healthy
     as the babies born from women who do not smoke. And some women would prefer having
      smaller babies.

                                   - Joseph Cullman, Philip Morris’ Chairman of the Board
                              ...on CBS’ Face the Nation, Jan 3, 1971

Fact check: the babies from women who smoke are not actually as healthy as the babies from women
who do not smoke.16





   14It is possible that there is a diﬀerence but we did not detect it. If there is a diﬀerence, we made a Type 2 Error.
  15We could have collected more data.  If the sample sizes are larger, we tend to have a better shot at ﬁnding a
diﬀerence if one exists. In fact, this is exactly what we would ﬁnd if we examined a larger data set!
  16You can watch an episode of John Oliver on Last Week Tonight to explore the present day oﬀenses of the tobacco
industry. Please be aware that there is some adult language: youtu.be/6UsHHOCH4q8.

---

# OpenIntro Statistics, 4th edition

## 7.3 — Difference of two means

### PDF page 272

272                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


            7.3.3  Case study: two versions of a course exam

             An instructor decided to run two slight variations of the same exam. Prior to passing out the
             exams, she shuﬄed the exams together to ensure each student received a random version. Summary
                 statistics for how students performed on these two exams are shown in Figure 7.16. Anticipating
              complaints from students who took Version B, she would like to evaluate whether the diﬀerence
              observed in the groups is so large that it provides convincing evidence that Version B was more
              diﬃcult (on average) than Version A.

                                           Version    n        ¯x    s  min  max
                          A         30   79.4  14    45   100
                            B         27   74.1  20    32   100

                              Figure 7.16: Summary statistics of scores for each exam version.



           GUIDED PRACTICE 7.28
             Construct hypotheses to evaluate whether the observed diﬀerence in sample means, ¯xA −¯xB = 5.3,
                   is due to chance. We will later evaluate these hypotheses using α = 0.01.17




           GUIDED PRACTICE 7.29
           To evaluate the hypotheses in Guided Practice 7.28 using the t-distribution, we must ﬁrst verify
               conditions.18

               (a) Does it seem reasonable that the scores are independent?

              (b) Any concerns about outliers?


                   After verifying the conditions for each sample and conﬁrming the samples are independent of
              each other, we are ready to conduct the test using the t-distribution. In this case, we are estimating
              the true diﬀerence in average test scores using the sample data, so the point estimate is ¯xA−¯xB = 5.3.
           The standard error of the estimate can be calculated as

                      s                                                     s2A    s2B  r 142   202                           SE =    +   =    +   = 4.62
                                      nA   nB      30    27

                Finally, we construct the test statistic:

                                      point estimate −null value    (79.4 −74.1) −0
                          T =                =          = 1.15
                                SE                     4.62

                    If we have a computer handy, we can identify the degrees of freedom as 45.97. Otherwise we use the
               smaller of n1 −1 and n2 −1: df = 26.





                  17H0: the exams are equally diﬃcult, on average. µA −µB = 0. HA: one exam was more diﬃcult than the other,
               on average. µA −µB̸ = 0.
                    18(a) Since the exams were shuﬄed, the “treatment” in this case was randomly assigned, so independence within
              and between groups is satisﬁed. (b) The summary statistics suggest the data are roughly symmetric about the mean,
              and the min/max values don’t suggest any outliers of concern.

---

# OpenIntro Statistics, 4th edition

## 7.3 — Difference of two means

### PDF page 273

7.3. DIFFERENCE OF TWO MEANS                                                              273



                                           T = 1.15




                     −3    −2    −1     0     1     2     3

        Figure 7.17: The t-distribution with 26 degrees of freedom and the p-value from
       exam example represented as the shaded areas.



EXAMPLE 7.30
Identify the p-value depicted in Figure 7.17 using df = 26, and provide a conclusion in the context
of the case study.

Using software, we can ﬁnd the one-tail area (0.13) and then double this value to get the two-tail
area, which is the p-value: 0.26. (Alternatively, we could use the t-table in Appendix C.2.)

In Guided Practice 7.28, we speciﬁed that we would use α = 0.01. Since the p-value is larger than
α, we do not reject the null hypothesis. That is, the data do not convincingly show that one exam
version is more diﬃcult than the other, and the teacher should not be convinced that she should
add points to the Version B exam scores.




7.3.4  Pooled standard deviation estimate (special topic)

     Occasionally, two populations will have standard deviations that are so similar that they can
be treated as identical. For example, historical data or a well-understood biological mechanism may
justify this strong assumption. In such cases, we can make the t-distribution approach slightly more
precise by using a pooled standard deviation.
    The pooled standard deviation of two groups is a way to use data from both samples to
better estimate the standard deviation and standard error. If s1 and s2 are the standard deviations
of groups 1 and 2 and there are very good reasons to believe that the population standard deviations
are equal, then we can obtain an improved estimate of the group variances by pooling their data:

                                        s21 × (n1 −1) + s22 × (n2 −1)                              s2pooled =
                                          n1 + n2 −2

where n1 and n2 are the sample sizes, as before. To use this new statistic, we substitute s2pooled in
place of s21 and s22 in the standard error formula, and we use an updated formula for the degrees of
freedom:

                                           df = n1 + n2 −2

    The beneﬁts of pooling the standard deviation are realized through obtaining a better estimate
of the standard deviation for each group and using a larger degrees of freedom parameter for the
t-distribution. Both of these changes may permit a more accurate model of the sampling distribution
of ¯x1 −¯x2, if the standard deviations of the two groups are indeed equal.


  POOL STANDARD DEVIATIONS ONLY AFTER CAREFUL CONSIDERATION
 A pooled standard deviation is only appropriate when background research indicates the pop-
  ulation standard deviations are nearly equal. When the sample size is large and the condition
  may be adequately checked with data, the beneﬁts of pooling the standard deviations greatly
  diminishes.

---

# OpenIntro Statistics, 4th edition

## 7.3 — Difference of two means

### PDF page 274

274                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


           Exercises


               7.23  Friday the 13th, Part I. In the early 1990’s, researchers in the UK collected data on traﬃc ﬂow, number
                 of shoppers, and traﬃc accident related emergency room admissions on Friday the 13th and the previous
                Friday, Friday the 6th. The histograms below show the distribution of number of cars passing by a speciﬁc
                 intersection on Friday the 6th and Friday the 13th for many such date pairs. Also given are some sample
                   statistics, where the diﬀerence is the number of cars on the 6th minus the number of cars on the 13th.19

                         4                                                3                                                5

                                                                                                                          4                         3
                                                                         2
                                                                                                                          3
                         2
                                                                                                                          2
                                                                         1
                         1                                                                                                                          1

                         0                                                0                                                0
                                 120000        130000        140000               120000        130000        140000          0            2000          4000

                                      Friday the 6th                                 Friday the 13th                                   Difference

                                                                6th       13th     Diﬀ.
                                                                                    ¯x   128,385   126,550   1,835
                                                   s    7,259     7,664    1,176
                                       n     10       10      10

                (a) Are there any underlying structures in these data that should be considered in an analysis? Explain.
                (b) What are the hypotheses for evaluating whether the number of people out on Friday the 6th is diﬀerent
                  than the number out on Friday the 13th?
                 (c) Check conditions to carry out the hypothesis test from part (b).
                (d) Calculate the test statistic and the p-value.
                 (e) What is the conclusion of the hypothesis test?
                  (f) Interpret the p-value in this context.
                (g) What type of error might have been made in the conclusion of your test? Explain.

               7.24  Diamonds, Part I. Prices of diamonds are determined by what is known as the 4 Cs: cut, clarity,
                  color, and carat weight. The prices of diamonds go up as the carat weight increases, but the increase is not
              smooth. For example, the diﬀerence between the size of a 0.99 carat diamond and a 1 carat diamond is
               undetectable to the naked human eye, but the price of a 1 carat diamond tends to be much higher than the
                 price of a 0.99 diamond. In this question we use two random samples of diamonds, 0.99 carats and 1 carat,
               each sample of size 23, and compare the average prices of the diamonds. In order to be able to compare
                equivalent units, we ﬁrst divide the price for each diamond by 100 times its weight in carats. That is, for
              a 0.99 carat diamond, we divide the price by 99. For a 1 carat diamond, we divide the price by 100. The
                 distributions and some sample statistics are shown below.20

             Conduct a hypothesis test to evaluate if there is a diﬀerence
                                                                        80              between the average standardized prices of 0.99 and 1 carat
              diamonds. Make sure to state your hypotheses clearly, check                                                                                                                                                                                                                               dollars)
                relevant conditions, and interpret your results in context of      60                                                                                    (in
               the data.
                          0.99 carats   1 carat                                                          price 40
             Mean                           $44.51
                                      $56.81                                                           Point            SD                           $13.32                                      $16.13
                                                                        20
              n          23        23
                                                                                          0.99 carats   1 carat





                    19T.J. Scanlon et al. “Is Friday the 13th Bad For Your Health?” In: BMJ 307 (1993), pp. 1584–1586.
                  20H. Wickham. ggplot2: elegant graphics for data analysis. Springer New York, 2009.

---

# OpenIntro Statistics, 4th edition

## 7.3 — Difference of two means

### PDF page 275

7.3. DIFFERENCE OF TWO MEANS                                                              275


7.25  Friday the 13th, Part II. The Friday the 13th study reported in Exercise 7.23 also provides data on
traﬃc accident related emergency room admissions. The distributions of these counts from Friday the 6th
and Friday the 13th are shown below for six such paired dates along with summary statistics. You may
assume that conditions for inference are met.

          2                                     2                                     2


          1                                     1                                     1


          0                                     0                                     0
                    5           10                   5           10                            −5           0
                  Friday the 6th                       Friday the 13th                         Difference

                                                  6th    13th    diﬀ
                            Mean    7.5   10.83   -3.33
                         SD     3.33    3.6    3.01
                              n        6      6      6

(a) Conduct a hypothesis test to evaluate if there is a diﬀerence between the average numbers of traﬃc
    accident related emergency room admissions between Friday the 6th and Friday the 13th.
(b) Calculate a 95% conﬁdence interval for the diﬀerence between the average numbers of traﬃc accident
     related emergency room admissions between Friday the 6th and Friday the 13th.
 (c) The conclusion of the original study states, “Friday 13th is unlucky for some. The risk of hospital
    admission as a result of a transport accident may be increased by as much as 52%. Staying at home is
    recommended.” Do you agree with this statement? Explain your reasoning.

7.26  Diamonds, Part II. In Exercise 7.24, we discussed diamond prices (standardized by weight) for diamonds with weights 0. 99 carats and 1 carat. See the table for summary statistics, and then construct a 95%
conﬁdence interval for the average diﬀerence between the standardized prices of 0.99 and 1 carat diamonds.
You may assume the conditions for inference are met.

                                               0.99 carats   1 carat
                            Mean     $44.51     $56.81
                          SD       $13.32     $16.13
                               n          23        23


7.27  Chicken diet and weight, Part I. Chicken farming is a multi-billion dollar industry, and any methods
that increase the growth rate of young chicks can reduce consumer costs while increasing company proﬁts,
possibly by millions of dollars. An experiment was conducted to measure and compare the eﬀectiveness of
various feed supplements on the growth rate of chickens. Newly hatched chicks were randomly allocated into
six groups, and each group was given a diﬀerent feed supplement. Below are some summary statistics from
this data set along with box plots showing the distribution of weights by feed type.21


                                                                      G
   400                                                               G

   350

                                                                               casein       323.58   64.43   12grams) 300                                                              Mean   SD    n
                                                                       horsebean   160.20   38.63   10
(in
   250                                                                          linseed      218.75   52.24   12
                                                                      G          meatmeal   276.91   64.90   11Weight 200                                                               soybean     246.43   54.13   14
                                                                    sunﬂower    328.92   48.84   12
   150

   100
               casein  horsebean  linseed  meatmeal  soybean  sunflower

(a) Describe the distributions of weights of chickens that were fed linseed and horsebean.
(b) Do these data provide strong evidence that the average weights of chickens that were fed linseed and
    horsebean are diﬀerent? Use a 5% signiﬁcance level.
 (c) What type of error might we have committed? Explain.
(d) Would your conclusion change if we used α = 0.01?


   21Chicken Weights by Feed Type, from the datasets package in R..

---

# OpenIntro Statistics, 4th edition

## 7.3 — Difference of two means

### PDF page 276

276                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


               7.28  Fuel efﬁciency of manual and automatic cars, Part I. Each year the US Environmental Protection
             Agency (EPA) releases fuel economy data on cars manufactured in that year. Below are summary statistics
             on fuel eﬃciency (in miles/gallon) from random samples of cars with manual and automatic transmissions.
           Do these data provide strong evidence of a diﬀerence between the average fuel eﬃciency of cars with manual
             and automatic transmissions in terms of their average city mileage? Assume that conditions for inference
                are satisﬁed.22

                                                          35


                                 City MPG
                          Automatic  Manual               25
                Mean     16.12       19.85
              SD         3.58        4.51
                 n          26         26
                                                          15


                                                                           automatic        manual

                                                                                              City MPG

               7.29  Chicken diet and weight, Part II. Casein is a common weight gain supplement for humans. Does it
              have an eﬀect on chickens? Using data provided in Exercise 7.27, test the hypothesis that the average weight
                 of chickens that were fed casein is diﬀerent than the average weight of chickens that were fed soybean.  If
              your hypothesis test yields a statistically signiﬁcant result, discuss whether or not the higher average weight
                 of chickens can be attributed to the casein diet. Assume that conditions for inference are satisﬁed.

               7.30  Fuel efﬁciency of manual and automatic cars, Part II. The table provides summary statistics on
              highway fuel economy of the same 52 cars from Exercise 7.28.  Use these statistics to calculate a 98%
              conﬁdence interval for the diﬀerence between average highway mileage of manual and automatic cars, and
                 interpret this interval in the context of the data.23

                                                          35


                       Hwy MPG
                          Automatic  Manual               25
                Mean     22.92       27.88
              SD         5.29        5.01
                 n          26         26
                                                          15


                                                                           automatic        manual

                                                              Hwy MPG





                   22U.S. Department of Energy, Fuel Economy Data, 2012 Dataﬁle.
                   23U.S. Department of Energy, Fuel Economy Data, 2012 Dataﬁle.

---

# OpenIntro Statistics, 4th edition

## 7.3 — Difference of two means

### PDF page 277

7.3. DIFFERENCE OF TWO MEANS                                                              277


7.31  Prison isolation experiment, Part I. Subjects from Central Prison in Raleigh, NC, volunteered for
an experiment involving an “isolation” experience. The goal of the experiment was to ﬁnd a treatment
that reduces subjects’ psychopathic deviant T scores. This score measures a person’s need for control or
their rebellion against control, and it is part of a commonly used mental health test called the Minnesota
Multiphasic Personality Inventory (MMPI) test. The experiment had three treatment groups:

(1) Four hours of sensory restriction plus a 15 minute “therapeutic” tape advising that professional help is
     available.
(2) Four hours of sensory restriction plus a 15 minute “emotionally neutral” tape on training hunting dogs.
(3) Four hours of sensory restriction but no taped message.

Forty-two subjects were randomly assigned to these treatment groups, and an MMPI test was administered
before and after the treatment. Distributions of the diﬀerences between pre and post treatment scores (pre
- post) are shown below, along with some sample statistics. Use this information to independently test the
eﬀectiveness of each treatment. Make sure to clearly state your hypotheses, check conditions, and interpret
results in the context of the data.24



   6                                                    4                                                4

   4
                                                    2                                                2
   2

   0                                                0                                                0
             0             20            40           −20      −10       0       10       20                 −20        −10          0

                 Treatment 1                                 Treatment 2                                 Treatment 3

                                         Tr 1   Tr 2   Tr 3
                             Mean   6.21   2.86   -3.21
                          SD      12.3   7.94    8.57
                               n        14    14     14


7.32  True / False: comparing means. Determine if the following statements are true or false, and explain
your reasoning for statements you identify as false.

(a) When comparing means of two samples where n1 = 20 and n2 = 40, we can use the normal model for
    the diﬀerence in means since n2 ≥30.
(b) As the degrees of freedom increases, the t-distribution approaches normality.
(c) We use a pooled standard error for calculating the standard error of the diﬀerence between means when
    sample sizes of groups are equal to each other.





   24Prison isolation experiment, stat.duke.edu/resources/datasets/prison-isolation.

---

# OpenIntro Statistics, 4th edition

## 7.4 — Power calculations for a difference of means

### PDF page 278

278                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


        7.4  Power calculations for a difference of means



             Often times in experiment planning, there are two competing considerations:

                • We want to collect enough data that we can detect important eﬀects.

                • Collecting data can be expensive, and in experiments involving people, there may be some risk
                    to patients.

              In this section, we focus on the context of a clinical trial, which is a health-related experiment where
              the subject are people, and we will determine an appropriate sample size where we can be 80% sure
              that we would detect any practically important eﬀects.25


            7.4.1  Going through the motions of a test

                 We’re going to go through the motions of a hypothesis test.  This will help us frame our
               calculations for determining an appropriate sample size for the study.


          EXAMPLE 7.31
             Suppose a pharmaceutical company has developed a new drug for lowering blood pressure, and they
               are preparing a clinical trial (experiment) to test the drug’s eﬀectiveness. They recruit people who
               are taking a particular standard blood pressure medication. People in the control group will continue
               to take their current medication through generic-looking pills to ensure blinding. Write down the
              hypotheses for a two-sided hypothesis test in this context.

               Generally, clinical trials use a two-sided alternative hypothesis, so below are suitable hypotheses for
                this context:

            H0: The new drug performs exactly as well as the standard medication.
                   µtrmt −µctrl = 0.
           HA: The new drug’s performance diﬀers from the standard medication.
                   µtrmt −µctrl̸ = 0.


          EXAMPLE 7.32
           The researchers would like to run the clinical trial on patients with systolic blood pressures between
             140 and 180 mmHg. Suppose previously published studies suggest that the standard deviation of the
                patients’ blood pressures will be about 12 mmHg and the distribution of patient blood pressures will
             be approximately symmetric.26  If we had 100 patients per group, what would be the approximate
              standard error for ¯xtrmt −¯xctrl?

           The standard error is calculated as follows:

                       s                                                        s2trmt    s2ctrl  r 122   122
                                          SE¯xtrmt−¯xctrl =     +   =    +   = 1.70
                                                     ntrmt    nctrl     100   100

             This may be an imperfect estimate of SE¯xtrmt−¯xctrl, since the standard deviation estimate we used
           may not be perfectly correct for this group of patients. However, it is suﬃcient for our purposes.



                 25Even though we don’t cover it explicitly, similar sample size planning is also helpful for observational studies.
                   26In this particular study, we’d generally measure each patient’s blood pressure at the beginning and end of the
                  study, and then the outcome measurement for the study would be the average change in blood pressure. That is, both
               µtrmt and µctrl would represent average diﬀerences. This is what you might think of as a 2-sample paired testing
                  structure, and we’d analyze it exactly just like a hypothesis test for a diﬀerence in the average change for patients.
                 In the calculations we perform here, we’ll suppose that 12 mmHg is the predicted standard deviation of a patient’s
                blood pressure diﬀerence over the course of the study.

---

# OpenIntro Statistics, 4th edition

## 7.4 — Power calculations for a difference of means

### PDF page 279

7.4. POWER CALCULATIONS FOR A DIFFERENCE OF MEANS                                   279



EXAMPLE 7.33
What does the null distribution of ¯xtrmt −¯xctrl look like?

The degrees of freedom are greater than 30, so the distribution of ¯xtrmt −¯xctrl will be approximately
normal. The standard deviation of this distribution (the standard error) would be about 1.70, and
under the null hypothesis, its mean would be 0.

                                                           Null distribution





        −9        −6        −3         0         3         6         9
                                                              xtrmt −xctrl


EXAMPLE 7.34
For what values of ¯xtrmt −¯xctrl would we reject the null hypothesis?

For α = 0.05, we would reject H0 if the diﬀerence is in the lower 2.5% or upper 2.5% tail:

Lower 2.5%: For the normal model, this is 1.96 standard errors below 0, so any diﬀerence smaller
     than −1.96 × 1.70 = −3.332 mmHg.

Upper 2.5%: For the normal model, this is 1.96 standard errors above 0, so any diﬀerence larger
     than 1.96 × 1.70 = 3.332 mmHg.


The boundaries of these rejection regions are shown below:

                                                           Null distribution


                                 Do not                   Reject H0                                        Reject H0                                                   reject H0

        −9        −6        −3         0         3         6         9
                                                              xtrmt −xctrl


     Next, we’ll perform some hypothetical calculations to determine the probability we reject the
null hypothesis, if the alternative hypothesis were actually true.


7.4.2  Computing the power for a 2-sample test

   When planning a study, we want to know how likely we are to detect an eﬀect we care about.
In other words, if there is a real eﬀect, and that eﬀect is large enough that it has practical value,
then what’s the probability that we detect that eﬀect? This probability is called the power, and
we can compute it for diﬀerent sample sizes or for diﬀerent eﬀect sizes.
   We ﬁrst determine what is a practically signiﬁcant result. Suppose that the company researchers
care about ﬁnding any eﬀect on blood pressure that is 3 mmHg or larger vs the standard medication.
Here, 3 mmHg is the minimum eﬀect size of interest, and we want to know how likely we are to
detect this size of an eﬀect in the study.

---

# OpenIntro Statistics, 4th edition

## 7.4 — Power calculations for a difference of means

### PDF page 280

280                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA



          EXAMPLE 7.35
             Suppose we decided to move forward with 100 patients per treatment group and the new drug
              reduces blood pressure by an additional 3 mmHg relative to the standard medication. What is the
               probability that we detect a drop?

              Before we even do any calculations, notice that if ¯xtrmt −¯xctrl = −3 mmHg, there wouldn’t even be
             suﬃcient evidence to reject H0. That’s not a good sign.

           To calculate the probability that we will reject H0, we need to determine a few things:

                • The sampling distribution for ¯xtrmt −¯xctrl when the true diﬀerence is -3 mmHg. This is the
                 same as the null distribution, except it is shifted to the left by 3:

                                   Distribution with                              Null distribution
                                           µtrmt −µctrl = −3




                      −9         −6         −3          0          3          6          9
                                                                                             xtrmt −xctrl


                • The rejection regions, which are outside of the dotted lines above.

                • The fraction of the distribution that falls in the rejection region.


              In short, we need to calculate the probability that x < −3.332 for a normal distribution with mean
                -3 and standard deviation 1.7. To do so, we ﬁrst shade the area we want to calculate:

                                Distribution with                            Null distribution
                                       µtrmt −µctrl = −3




                    −9        −6        −3         0         3         6         9
                                                                                   xtrmt −xctrl


               We’ll use a normal approximation, which is good approximation when the degrees of freedom is
             about 30 or more. We’ll start by calculating the Z-score and ﬁnd the tail area using either statistical
              software or the probability table:

                                        −3.332 −(−3)
                           Z =         = −0.20  →     0.42
                                                      1.7

           The power for the test is about 42% when µtrmt −µctrl = −3 and each group has a sample size
                of 100.

                   In Example 7.35, we ignored the upper rejection region in the calculation, which was in the
              opposite direction of the hypothetical truth, i.e. -3. The reasoning? There wouldn’t be any value in
                rejecting the null hypothesis and concluding there was an increase when in fact there was a decrease.
                 We’ve also used a normal distribution instead of the t-distribution. This is a convenience, and
                      if the sample size is too small, we’d need to revert back to using the t-distribution. We’ll discuss
                this a bit further at the end of this section.

---

# OpenIntro Statistics, 4th edition

## 7.4 — Power calculations for a difference of means

### PDF page 281

7.4. POWER CALCULATIONS FOR A DIFFERENCE OF MEANS                                   281


7.4.3  Determining a proper sample size

     In the last example, we found that  if we have a sample size of 100 in each group, we can
only detect an eﬀect size of 3 mmHg with a probability of about 0.42. Suppose the researchers
moved forward and only used 100 patients per group, and the data did not support the alternative
hypothesis, i.e. the researchers did not reject H0. This is a very bad situation to be in for a few
reasons:

   • In the back of the researchers’ minds, they’d all be wondering, maybe there is a real and
     meaningful diﬀerence, but we weren’t able to detect it with such a small sample.

   • The company probably invested hundreds of millions of dollars in developing the new drug, so
    now they are left with great uncertainty about its potential since the experiment didn’t have
     a great shot at detecting eﬀects that could still be important.

   • Patients were subjected to the drug, and we can’t even say with much certainty that the drug
      doesn’t help (or harm) patients.

   • Another clinical trial may need to be run to get a more conclusive answer as to whether the
     drug does hold any practical value, and conducting a second clinical trial may take years and
    many millions of dollars.

We want to avoid this situation, so we need to determine an appropriate sample size to ensure we can
be pretty conﬁdent that we’ll detect any eﬀects that are practically important. As mentioned earlier,
a change of 3 mmHg was deemed to be the minimum diﬀerence that was practically important. As a
ﬁrst step, we could calculate power for several diﬀerent sample sizes.  For instance, let’s try 500
patients per group.


GUIDED PRACTICE 7.36
Calculate the power to detect a change of -3 mmHg when using a sample size of 500 per group.27

(a) Determine the standard error (recall that the standard deviation for patients was expected to
    be about 12 mmHg).

(b) Identify the null distribution and rejection regions.

(c) Identify the alternative distribution when µtrmt −µctrl = −3.

(d) Compute the probability we reject the null hypothesis.


    The researchers decided 3 mmHg was the minimum diﬀerence that was practically important,
and with a sample size of 500, we can be very certain (97.7% or better) that we will detect any such
diﬀerence. We now have moved to another extreme where we are exposing an unnecessary number
of patients to the new drug in the clinical trial. Not only is this ethically questionable, but it would
also cost a lot more money than is necessary to be quite sure we’d detect any important eﬀects.
    The most common practice is to identify the sample size where the power is around 80%, and
sometimes 90%. Other values may be reasonable for a speciﬁc context, but 80% and 90% are most
commonly targeted as a good balance between high power and not exposing too many patients to a
new treatment (or wasting too much money).
   We could compute the power of the test at several other possible sample sizes until we ﬁnd one
that’s close to 80%, but there’s a better way. We should solve the problem backwards.

   27(a) The standard error is given as SE = q 122500 + 122500 = 0.76.
(b) & (c) The null distribution, rejection boundaries, and alternative distribution are shown below:
                  Distribution with                      Null distribution
                       µtrmt −µctrl = −3


       −9        −6        −3         0         3         6         9
                                                              xtrmt −xctrl
The rejection regions are the areas on the outside of the two dotted lines and are at ±0.76 × 1.96 = ±1.49.
(d) The area of the alternative distribution where µtrmt −µctrl = −3 has been shaded. We compute the Z-score and
ﬁnd the tail area: Z = −1.49−(−3)0.76   = 1.99 →0.977. With 500 patients per group, we would be about 97.7% sure
(or more) that we’d detect any eﬀects that are at least 3 mmHg in size.

---

# OpenIntro Statistics, 4th edition

## 7.4 — Power calculations for a difference of means

### PDF page 282

282                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA



          EXAMPLE 7.37
           What sample size will lead to a power of 80%?

               We’ll assume we have a large enough sample that the normal distribution is a good approximation
                for the test statistic, since the normal distribution and the t-distribution look almost identical when
              the degrees of freedom are moderately large (e.g. df ≥30). If that doesn’t turn out to be true, then
             we’d need to make a correction.

         We start by identifying the Z-score that would give us a lower tail of 80%. For a moderately large
             sample size per group, the Z-score for a lower tail of 80% would be about Z = 0.84.

                                  Distribution with                       Null distribution
                                          µtrmt −µctrl = −3

                                                              0.84 SE   1.96 SE

                    −9        −6        −3         0         3         6         9
                                                                                   xtrmt −xctrl


               Additionally, the rejection region extends 1.96 × SE from the center of the null distribution for
          α = 0.05. This allows us to calculate the target distance between the center of the null and alternative
               distributions in terms of the standard error:

                                              0.84 × SE + 1.96 × SE = 2.8 × SE

              In our example, we want the distance between the null and alternative distributions’ centers to equal
              the minimum eﬀect size of interest, 3 mmHg, which allows us to set up an equation between this
              diﬀerence and the standard error:

                                          3 = 2.8 × SE
                         r 122   122
                                          3 = 2.8 ×    +
                                             n    n
                                                       2.82
                                   n =   × 122 + 122 = 250.88
                                                    32


         We should target 251 patients per group in order to achieve 80% power at the 0.05 signiﬁcance level
                for this context.

               The standard error diﬀerence of 2.8 × SE is speciﬁc to a context where the targeted power is
           80% and the signiﬁcance level is α = 0.05.  If the targeted power is 90% or if we use a diﬀerent
              signiﬁcance level, then we’ll use something a little diﬀerent than 2.8 × SE.
              Had the suggested sample size been relatively small – roughly 30 or smaller – it would have
             been a good idea to rework the calculations using the degrees of fredom for the smaller sample size
             under that initial sample size. That is, we would have revised the 0.84 and 1.96 values based on
              degrees of freedom implied by the initial sample size. The revised sample size target would generally
             have then been a little larger.

---

# OpenIntro Statistics, 4th edition

## 7.4 — Power calculations for a difference of means

### PDF page 283

7.4. POWER CALCULATIONS FOR A DIFFERENCE OF MEANS                                   283



GUIDED PRACTICE 7.38
Suppose the targeted power was 90% and we were using α = 0.01. How many standard errors should
separate the centers of the null and alternative distribution, where the alternative distribution is
centered at the minimum eﬀect size of interest?28



GUIDED PRACTICE 7.39
What are some considerations that are important in determining what the power should be for an
experiment?29


     Figure 7.18 shows the power for sample sizes from 20 patients to 5,000 patients when α = 0.05
and the true diﬀerence is -3. This curve was constructed by writing a program to compute the power
for many diﬀerent sample sizes.


           1.0

           0.8

           0.6
         Power           0.4

           0.2

           0.0
              20        50     100     200       500    1000    2000      5000

                                   Sample Size Per Group

        Figure 7.18: The curve shows the power for diﬀerent sample sizes in the context
         of the blood pressure example when the true diﬀerence is -3. Having more than
        about 250 to 350 observations doesn’t provide much additional value in detecting
       an eﬀect when α = 0.05.


    Power calculations for expensive or risky experiments are critical. However, what about experiments that are inexpensive and where the ethical considerations are minimal? For example, if we are
doing ﬁnal testing on a new feature on a popular website, how would our sample size considerations
change? As before, we’d want to make sure the sample is big enough. However, suppose the feature
has undergone some testing and is known to perform well (e.g. the website’s users seem to enjoy the
feature). Then it may be reasonable to run a larger experiment if there’s value from having a more
precise estimate of the feature’s eﬀect, such as helping guide the development of the next useful
feature.





   28First, ﬁnd the Z-score such that 90% of the distribution is below it: Z = 1.28. Next, ﬁnd the cutoﬀs for the
rejection regions: ±2.58. Then the diﬀerence in centers should be about 1.28 × SE + 2.58 × SE = 3.86 × SE.
  29Answers will vary, but here are a few important considerations:

    • Whether there is any risk to patients in the study.
    • The cost of enrolling more patients.
    • The potential downside of not detecting an eﬀect of interest.

---

# OpenIntro Statistics, 4th edition

## 7.4 — Power calculations for a difference of means

### PDF page 284

284                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


           Exercises


               7.33  Increasing corn yield. A large farm wants to try out a new type of fertilizer to evaluate whether
                     it will improve the farm’s corn production. The land is broken into plots that produce an average of 1,215
             pounds of corn with a standard deviation of 94 pounds per plot. The owner is interested in detecting any
               average diﬀerence of at least 40 pounds per plot. How many plots of land would be needed for the experiment
                        if the desired power level is 90%? Assume each plot of land gets treated with either the current fertilizer or
               the new fertilizer.

               7.34  Email outreach efforts. A medical research group is recruiting people to complete short surveys
              about their medical history. For example, one survey asks for information on a person’s family history in
               regards to cancer. Another survey asks about what topics were discussed during the person’s last visit to a
                 hospital. So far, as people sign up, they complete an average of just 4 surveys, and the standard deviation
                 of the number of surveys is about 2.2. The research group wants to try a new interface that they think will
               encourage new enrollees to complete more surveys, where they will randomize each enrollee to either get the
            new interface or the current interface. How many new enrollees do they need for each interface to detect an
               eﬀect size of 0.5 surveys per enrollee, if the desired power level is 80%?

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 285

7.5. COMPARING MANY MEANS WITH ANOVA                                                  285


7.5  Comparing many means with ANOVA



Sometimes we want to compare means across many groups. We might initially think to do pairwise
comparisons. For example, if there were three groups, we might be tempted to compare the ﬁrst
mean with the second, then with the third, and then ﬁnally compare the second and third means
for a total of three comparisons. However, this strategy can be treacherous. If we have many groups
and do many comparisons, it is likely that we will eventually ﬁnd a diﬀerence just by chance, even
if there is no diﬀerence in the populations. Instead, we should apply a holistic test to check whether
there is evidence that at least one pair groups are in fact diﬀerent, and this is where ANOVA saves
the day.


7.5.1  Core ideas of ANOVA

     In this section, we will learn a new method called analysis of variance (ANOVA) and a
new test statistic called F. ANOVA uses a single hypothesis test to check whether the means across
many groups are equal:

 H0: The mean outcome is the same across all groups. In statistical notation, µ1 = µ2 = · · · = µk
     where µi represents the mean of the outcome for observations in category i.
HA: At least one mean is diﬀerent.

Generally we must check three conditions on the data before performing ANOVA:

   • the observations are independent within and across groups,

   • the data within each group are nearly normal, and

   • the variability across the groups is about equal.

When these three conditions are met, we may perform an ANOVA to determine whether the data
provide strong evidence against the null hypothesis that all the µi are equal.


EXAMPLE 7.40
College departments commonly run multiple lectures of the same introductory course each semester
because of high demand. Consider a statistics department that runs three lectures of an introductory
statistics course. We might like to determine whether there are statistically signiﬁcant diﬀerences in
ﬁrst exam scores in these three classes (A, B, and C). Describe appropriate hypotheses to determine
whether there are any diﬀerences between the three classes.

The hypotheses may be written in the following form:

 H0: The average score is identical in all lectures. Any observed diﬀerence is due to chance. Nota-
      tionally, we write µA = µB = µC.
HA: The average score varies by class. We would reject the null hypothesis in favor of the alternative
     hypothesis if there were larger diﬀerences among the class averages than what we might expect
     from chance alone.

     Strong evidence favoring the alternative hypothesis in ANOVA is described by unusually large
diﬀerences among the group means. We will soon learn that assessing the variability of the group
means relative to the variability among individual observations within each group is key to ANOVA’s
success.

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 286

286                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA



          EXAMPLE 7.41
            Examine Figure 7.19. Compare groups I, II, and III. Can you visually determine if the diﬀerences in
              the group centers is due to chance or not? Now compare groups IV, V, and VI. Do these diﬀerences
             appear to be due to chance?

           Any real diﬀerence in the means of groups I, II, and III is diﬃcult to discern, because the data within
              each group are very volatile relative to any diﬀerences in the average outcome. On the other hand, it
             appears there are diﬀerences in the centers of groups IV, V, and VI. For instance, group V appears
               to have a higher mean than that of the other two groups. Investigating groups IV, V, and VI, we
               see the diﬀerences in the groups’ centers are noticeable because those diﬀerences are large relative
               to the variability in the individual observations within each group.




                             4

                             3

                             2
                                                                      Outcome                             1

                             0

                           −1

                                                                   IV     V       VI

                             Figure 7.19: Side-by-side dot plot for the outcomes for six groups.




            7.5.2  Is batting performance related to player position in MLB?

            We would like to discern whether there are real diﬀerences between the batting performance of
               baseball players according to their position: outﬁelder (OF), inﬁelder (IF), and catcher (C). We will
              use a data set called bat18, which includes batting records of 429 Major League Baseball (MLB)
               players from the 2018 season who had at least 100 at bats.  Six of the 429 cases represented in
            bat18 are shown in Figure 7.20, and descriptions for each variable are provided in Figure 7.21. The
             measure we will use for the player batting performance (the outcome variable) is on-base percentage
               (OBP). The on-base percentage roughly represents the fraction of the time a player successfully gets
            on base or hits a home run.

                      name          team   position  AB  H  HR  RBI  AVG  OBP
                       1  Abreu, J     CWS  IF       499  132   22    78    0.265   0.325
                       2  Acuna Jr., R   ATL  OF      433  127   26    64    0.293   0.366
                       3  Adames, W    TB    IF       288   80   10    34    0.278   0.348
                                                                                                                             ...             ...                                                                                 ...                                   ...                                                      ...                          ...                          ...                            ...
                     427  Zimmerman, R  WSH  IF       288   76   13    51    0.264   0.337
                     428   Zobrist, B     CHC   IF       455  139   9    58    0.305   0.378
                     429   Zunino, M     SEA  C        373   75   20    44    0.201   0.259

                                    Figure 7.20: Six cases from the bat18 data matrix.

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 287

7.5. COMPARING MANY MEANS WITH ANOVA                                                  287


                variable   description
               name       Player name
               team      The abbreviated name of the player’s team
               position  The player’s primary ﬁeld position (OF, IF, C)
               AB       Number of opportunities at bat
               H        Number of hits
               HR       Number of home runs
               RBI       Number of runs batted in
               AVG        Batting average, which is equal to H/AB
               OBP        On-base percentage, which is roughly equal to the fraction
                                of times a player gets on base or hits a home run

              Figure 7.21: Variables and their descriptions for the bat18 data set.



GUIDED PRACTICE 7.42
The null hypothesis under consideration is the following:  µOF = µIF = µC.  Write the null and
corresponding alternative hypotheses in plain language.30




EXAMPLE 7.43
The player positions have been divided into three groups: outﬁeld (OF), inﬁeld (IF), and catcher (C).
What would be an appropriate point estimate of the on-base percentage by outﬁelders, µOF?

A good estimate of the on-base percentage by outﬁelders would be the sample average of OBP for
just those players whose position is outﬁeld: ¯xOF = 0.320.


     Figure 7.22 provides summary statistics for each group. A side-by-side box plot for the onbase percentage is shown in Figure 7.23. Notice that the variability appears to be approximately
constant across groups; nearly constant variance across groups is an important assumption that
must be satisﬁed before we consider the ANOVA approach.

                                                OF     IF      C
                           Sample size (ni)      160    205     64
                           Sample mean (¯xi)   0.320   0.318   0.302
                           Sample SD (si)     0.043   0.038   0.038

         Figure 7.22: Summary statistics of on-base percentage, split by player position.



                           0.45

                           0.40

                           0.35                                                                               Percentage
                           0.30

                           0.25                                                        On−Base
                           0.20


                              OF              IF         C
                                                              Position

        Figure 7.23: Side-by-side box plot of the on-base percentage for 429 players across
         three groups. With over a hundred players in both the inﬁeld and outﬁeld groups,
        the apparent outliers are not a concern.


  30H0: The average on-base percentage is equal across the three positions. HA: The average on-base percentage
varies across some (or all) groups.

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 288

288                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA



          EXAMPLE 7.44
           The largest diﬀerence between the sample means is between the catcher and the outﬁelder positions.
              Consider again the original hypotheses:

             H0: µOF = µIF = µC
           HA: The average on-base percentage (µi) varies across some (or all) groups.

         Why might it be inappropriate to run the test by simply estimating whether the diﬀerence of µC
            and µOF is statistically signiﬁcant at a 0.05 signiﬁcance level?

           The primary issue here is that we are inspecting the data before picking the groups that will be
             compared.  It is inappropriate to examine all data by eye (informal testing) and only afterwards
              decide which parts to formally test. This is called data snooping or data ﬁshing.  Naturally,
           we would pick the groups with the large diﬀerences for the formal test, and this would leading to
            an inﬂation in the Type 1 Error rate. To understand this better, let’s consider a slightly diﬀerent
              problem.

             Suppose we are to measure the aptitude for students in 20 classes in a large elementary school at
              the beginning of the year. In this school, all students are randomly assigned to classrooms, so any
              diﬀerences we observe between the classes at the start of the year are completely due to chance.
             However, with so many groups, we will probably observe a few groups that look rather diﬀerent from
              each other. If we select only these classes that look so diﬀerent and then perform a formal test, we
                 will probably make the wrong conclusion that the assignment wasn’t random. While we might only
              formally test diﬀerences for a few pairs of classes, we informally evaluated the other classes by eye
               before choosing the most extreme cases for a comparison.


                  For additional information on the ideas expressed in Example 7.44, we recommend reading
             about the prosecutor’s fallacy.31
                   In the next section we will learn how to use the F statistic and ANOVA to test whether observed
              diﬀerences in sample means could have happened just by chance even if there was no diﬀerence in
              the respective population means.





                    31See, for example, statmodeling.stat.columbia.edu/2007/05/18/the prosecutors.

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 289

7.5. COMPARING MANY MEANS WITH ANOVA                                                  289


7.5.3  Analysis of variance (ANOVA) and the F -test

    The method of analysis of variance in this context focuses on answering one question:  is the
variability in the sample means so large that it seems unlikely to be from chance alone? This question
is diﬀerent from earlier testing procedures since we will simultaneously consider many groups, and
evaluate whether their sample means diﬀer more than we would expect from natural variation.
We call this variability the mean square between groups (MSG), and it has an associated
degrees of freedom, dfG = k −1 when there are k groups. The MSG can be thought of as a scaled
variance formula for means. If the null hypothesis is true, any variation in the sample means is due
to chance and shouldn’t be too large. Details of MSG calculations are provided in the footnote.32
However, we typically use software for these computations.
    The mean square between the groups is, on its own, quite useless in a hypothesis test. We need
a benchmark value for how much variability should be expected among the sample means if the
null hypothesis is true. To this end, we compute a pooled variance estimate, often abbreviated as
the mean square error (MSE), which has an associated degrees of freedom value dfE = n −k.
It is helpful to think of MSE as a measure of the variability within the groups.  Details of the
computations of the MSE and a link to an extra online section for ANOVA calculations are provided
in the footnote33 for interested readers.
   When the null hypothesis is true, any diﬀerences among the sample means are only due to
chance, and the MSG and MSE should be about equal. As a test statistic for ANOVA, we examine
the fraction of MSG and MSE:

                         MSG
                              F =
                          MSE

The MSG represents a measure of the between-group variability, and MSE measures the variability
within each of the groups.


GUIDED PRACTICE 7.45
For the baseball data, MSG = 0.00803 and MSE = 0.00158.  Identify the degrees of freedom
associated with MSG and MSE and verify the F statistic is approximately 5.077.34


   We can use the F statistic to evaluate the hypotheses in what is called an F -test. A p-value
can be computed from the F statistic using an F distribution, which has two associated parameters:
df1 and df2. For the F statistic in ANOVA, df1 = dfG and df2 = dfE. An F distribution with 2 and
426 degrees of freedom, corresponding to the F statistic for the baseball hypothesis test, is shown
in Figure 7.24.




   32Let ¯x represent the mean of outcomes across all groups. Then the mean square between groups is computed as

                                         1          1    k
                   MSG =   SSG =  X ni (¯xi −¯x)2
                                        dfG       k −1 i=1

where SSG is called the sum of squares between groups and ni is the sample size of group i.
   33Let ¯x represent the mean of outcomes across all groups. Then the sum of squares total (SST) is computed as

                                              n
                                 SST = X (xi −¯x)2
                                                    i=1

where the sum is over all observations in the data set. Then we compute the sum of squared errors (SSE) in one
of two equivalent ways:

                     SSE = SST −SSG
                      = (n1 −1)s21 + (n2 −1)s22 + · · · + (nk −1)s2k
where s2i  is the sample variance (square of the standard deviation) of the residuals in group i. Then the MSE is the
standardized form of SSE: MSE =  1 SSE.
                                     dfE
For additional details on ANOVA calculations, see www.openintro.org/d?ﬁle=stat extra anova calculations
  34There are k = 3 groups, so dfG = k −1 = 2. There are n = n1 + n2 + n3 = 429 total observations, so dfE =
n−k = 426. Then the F statistic is computed as the ratio of MSG and MSE: F = MSEMSG = 0.001580.00803 = 5.082 ≈5.077.
(F = 5.077 was computed by using values for MSG and MSE that were not rounded.)

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 290

290                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA





                                                                           Small tail area



                                       0          2          4          6          8

                                Figure 7.24: An F distribution with df1 = 2 and df2 = 426.


               The larger the observed variability in the sample means (MSG) relative to the within-group
               observations (MSE), the larger F will be and the stronger the evidence against the null hypothesis.
             Because larger values of F represent stronger evidence against the null hypothesis, we use the upper
                  tail of the distribution to compute a p-value.


             THE F STATISTIC AND THE F -TEST
                Analysis of variance (ANOVA) is used to test whether the mean outcome diﬀers across 2 or
              more groups. ANOVA uses a test statistic F, which represents a standardized ratio of variability
                  in the sample means relative to the variability within the groups. If H0 is true and the model
                 conditions are satisﬁed, the statistic F follows an F distribution with parameters df1 = k −1
              and df2 = n −k. The upper tail of the F distribution is used to represent the p-value.



          EXAMPLE 7.46
           The p-value corresponding to the shaded area in Figure 7.24 is equal to about 0.0066. Does this
              provide strong evidence against the null hypothesis?

           The p-value is smaller than 0.05, indicating the evidence is strong enough to reject the null hypothesis
               at a signiﬁcance level of 0.05. That is, the data provide strong evidence that the average on-base
              percentage varies by player’s primary ﬁeld position.



            7.5.4  Reading an ANOVA table from software

               The calculations required to perform an ANOVA by hand are tedious and prone to human
                error. For these reasons, it is common to use statistical software to calculate the F statistic and
               p-value.
             An ANOVA can be summarized in a table very similar to that of a regression summary, which
           we will see in Chapters 8 and 9. Figure 7.25 shows an ANOVA summary to test whether the mean of
              on-base percentage varies by player positions in the MLB. Many of these values should look familiar;
                in particular, the F-test statistic and p-value can be retrieved from the last two columns.

                                        Df  Sum Sq  Mean Sq  F value  Pr(>F)
                                    position      2    0.0161     0.0080    5.0766    0.0066
                                  Residuals  426    0.6740     0.0016
                                                                          spooled = 0.040 on df = 423

                      Figure 7.25: ANOVA summary for testing whether the average on-base percentage
                       diﬀers across player positions.

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 291

7.5. COMPARING MANY MEANS WITH ANOVA                                                  291


7.5.5  Graphical diagnostics for an ANOVA analysis

    There are three conditions we must check for an ANOVA analysis:  all observations must be
independent, the data in each group must be nearly normal, and the variance within each group
must be approximately equal.

Independence. If the data are a simple random sample, this condition is satisﬁed. For processes
     and experiments, carefully consider whether the data may be independent (e.g. no pairing).
     For example, in the MLB data, the data were not sampled. However, there are not obvious
      reasons why independence would not hold for most or all observations.

Approximately normal. As with one- and two-sample testing for means, the normality assump-
      tion is especially important when the sample size is quite small when it is ironically diﬃcult
      to check for non-normality. A histogram of the observations from each group is shown in Fig-
     ure 7.26. Since each of the groups we’re considering have relatively large sample sizes, what
      we’re looking for are major outliers. None are apparent, so this conditions is reasonably met.

            Outfielders                    In−fielders                  Catchers
                                    50                              14    40
                                    40                              12
    30                                                               10
                                    30                               8
    20                                    20                               6 Frequency                                                                                                             Frequency                                                                                                             Frequency  4    10                              10                                                                      2
     0                               0                               0
            0.2      0.3      0.4                  0.2      0.3      0.4                  0.2      0.3      0.4
          On−Base Percentage              On−Base Percentage              On−Base Percentage

                    Figure 7.26: Histograms of OBP for each ﬁeld position.


Constant variance. The last assumption is that the variance in the groups is about equal from
     one group to the next. This assumption can be checked by examining a side-by-side box plot
      of the outcomes across the groups, as in Figure 7.23 on page 287. In this case, the variability
       is similar in the four groups but not identical. We see in Table 7.22 on page 287 that the
     standard deviation doesn’t vary much from one group to the next.



  DIAGNOSTICS FOR AN ANOVA ANALYSIS
  Independence is always important to an ANOVA analysis. The normality condition is very
  important when the sample sizes for each group are relatively small. The constant variance
  condition is especially important when the sample sizes diﬀer between groups.

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 292

292                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


            7.5.6  Multiple comparisons and controlling Type 1 Error rate

             When we reject the null hypothesis in an ANOVA analysis, we might wonder, which of these
             groups have diﬀerent means? To answer this question, we compare the means of each possible pair
                of groups. For instance, if there are three groups and there is strong evidence that there are some
              diﬀerences in the group means, there are three comparisons to make: group 1 to group 2, group 1
               to group 3, and group 2 to group 3. These comparisons can be accomplished using a two-sample
                  t-test, but we use a modiﬁed signiﬁcance level and a pooled estimate of the standard deviation across
              groups. Usually this pooled standard deviation can be found in the ANOVA table, e.g. along the
            bottom of Figure 7.25.


          EXAMPLE 7.47
            Example 7.40 on page 285 discussed three statistics lectures, all taught during the same semester.
              Figure 7.27 shows summary statistics for these three courses, and a side-by-side box plot of the data
                   is shown in Figure 7.28. We would like to conduct an ANOVA for these data. Do you see any
               deviations from the three conditions for ANOVA?

              In this case (like many others) it is diﬃcult to check independence in a rigorous way.  Instead,
              the best we can do is use common sense to consider reasons the assumption of independence may
             not hold.  For instance, the independence assumption may not be reasonable  if there is a star
              teaching assistant that only half of the students may access; such a scenario would divide a class
               into two subgroups. No such situations were evident for these particular data, and we believe that
             independence is acceptable.

           The distributions in the side-by-side box plot appear to be roughly symmetric and show no noticeable
                 outliers.

           The box plots show approximately equal variability, which can be veriﬁed in Figure 7.27, supporting
              the constant variance assumption.



                                                 Class i   A   B   C
                                                  ni        58    55    51
                                                                              ¯xi       75.1   72.0   78.9
                                                           si        13.9   13.8   13.1

                      Figure 7.27: Summary statistics for the ﬁrst midterm scores in three diﬀerent
                         lectures of the same course.


                           100


                            80                                                         Scores

                            60                                                                   Midterm

                            40
                                   A           B          C

                                                              Lecture

                      Figure 7.28: Side-by-side box plot for the ﬁrst midterm scores in three diﬀerent
                         lectures of the same course.

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 293

7.5. COMPARING MANY MEANS WITH ANOVA                                                  293



GUIDED PRACTICE 7.48
ANOVA was conducted for the midterm data, and summary results are shown in Figure 7.29. What
should we conclude?35



                           Df  Sum Sq  Mean Sq  F value  Pr(>F)
                     lecture       2    1290.11     645.06      3.48    0.0330
                   Residuals  161   29810.13     185.16
                                                          spooled = 13.61 on df = 161

                  Figure 7.29: ANOVA summary table for the midterm data.

    There is strong evidence that the diﬀerent means in each of the three classes is not simply due
to chance. We might wonder, which of the classes are actually diﬀerent? As discussed in earlier
chapters, a two-sample t-test could be used to test for diﬀerences in each possible pair of groups.
However, one pitfall was discussed in Example 7.44 on page 288: when we run so many tests, the
Type 1 Error rate increases. This issue is resolved by using a modiﬁed signiﬁcance level.


  MULTIPLE COMPARISONS AND THE BONFERRONI CORRECTION FOR α
  The scenario of testing many pairs of groups is called multiple comparisons. The Bonferroni
  correction suggests that a more stringent signiﬁcance level is more appropriate for these tests:

                           α⋆= α/K

  where K is the number of comparisons being considered (formally or informally).  If there are
  k groups, then usually all possible pairs are compared and K = k(k−1)2    .



EXAMPLE 7.49
In Guided Practice 7.48, you found strong evidence of diﬀerences in the average midterm grades
between the three lectures. Complete the three possible pairwise comparisons using the Bonferroni
correction and report any diﬀerences.

We use a modiﬁed signiﬁcance level of α⋆= 0.05/3 = 0.0167.  Additionally, we use the pooled
estimate of the standard deviation: spooled = 13.61 on df = 161, which is provided in the ANOVA
summary table.

Lecture A versus Lecture B: The estimated diﬀerence and standard error are, respectively,

                          r 13.612   13.612
               ¯xA −¯xB = 75.1 −72 = 3.1        SE =      +    = 2.56
                                                        58      55

(See Section 7.3.4 on page 273 for additional details.) This results in a T-score of 1.21 on df = 161
(we use the df associated with spooled). Statistical software was used to precisely identify the twosided p-value since the modiﬁed signiﬁcance level of 0.0167 is not found in the t-table. The p-value
(0.228) is larger than α∗= 0.0167, so there is not strong evidence of a diﬀerence in the means of
lectures A and B.

Lecture A versus Lecture C: The estimated diﬀerence and standard error are 3.8 and 2.61, respectively. This results in a T score of 1.46 on df = 161 and a two-sided p-value of 0.1462. This p-value
is larger than α∗, so there is not strong evidence of a diﬀerence in the means of lectures A and C.

Lecture B versus Lecture C: The estimated diﬀerence and standard error are 6.9 and 2.65, respectively. This results in a T score of 2.60 on df = 161 and a two-sided p-value of 0.0102. This p-value
is smaller than α∗. Here we ﬁnd strong evidence of a diﬀerence in the means of lectures B and C.




  35The p-value of the test is 0.0330, less than the default signiﬁcance level of 0.05. Therefore, we reject the null
hypothesis and conclude that the diﬀerence in the average midterm scores are not due to chance.

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 294

294                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


         We might summarize the ﬁndings of the analysis from Example 7.49 using the following notation:

                        µA ?= µB             µA ?= µC                    µB̸ = µC

           The midterm mean in lecture A is not statistically distinguishable from those of lectures B or C.
             However, there is strong evidence that lectures B and C are diﬀerent.  In the ﬁrst two pairwise
              comparisons, we did not have suﬃcient evidence to reject the null hypothesis. Recall that failing to
                reject H0 does not imply H0 is true.


             REJECT H0H0H0 WITH ANOVA BUT FIND NO DIFFERENCES IN GROUP MEANS
                    It is possible to reject the null hypothesis using ANOVA and then to not subsequently identify
                 diﬀerences in the pairwise comparisons. However, this does not invalidate the ANOVA conclu-
                  sion. It only means we have not been able to successfully identify which speciﬁc groups diﬀer
                  in their means.


               The ANOVA procedure examines the big picture:  it considers all groups simultaneously to
              decipher whether there is evidence that some diﬀerence exists. Even if the test indicates that there
                   is strong evidence of diﬀerences in group means, identifying with high conﬁdence a speciﬁc diﬀerence
               as statistically signiﬁcant is more diﬃcult.
                  Consider the following analogy: we observe a Wall Street ﬁrm that makes large quantities of
           money based on predicting mergers. Mergers are generally diﬃcult to predict, and if the prediction
               success rate is extremely high, that may be considered suﬃciently strong evidence to warrant inves-
               tigation by the Securities and Exchange Commission (SEC). While the SEC may be quite certain
              that there is insider trading taking place at the ﬁrm, the evidence against any single trader may not
             be very strong. It is only when the SEC considers all the data that they identify the pattern. This
                   is eﬀectively the strategy of ANOVA: stand back and consider all the groups simultaneously.

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 295

7.5. COMPARING MANY MEANS WITH ANOVA                                                  295


Exercises


7.35   Fill in the blank. When doing an ANOVA, you observe large diﬀerences in means between groups.
Within the ANOVA framework, this would most likely be interpreted as evidence strongly favoring the
               hypothesis.

7.36  Which test? We would like to test if students who are in the social sciences, natural sciences, arts
and humanities, and other ﬁelds spend the same amount of time studying for this course. What type of test
should we use? Explain your reasoning.

7.37  Chicken diet and weight, Part III. In Exercises 7.27 and 7.29 we compared the eﬀects of two types
of feed at a time. A better analysis would ﬁrst consider all feed types at once: casein, horsebean, linseed,
meat meal, soybean, and sunﬂower. The ANOVA output below can be used to test for diﬀerences between
the average weights of chicks on diﬀerent diets.

                             Df    Sum Sq   Mean Sq  F value  Pr(>F)
                       feed         5   231,129.16   46,225.83     15.36    0.0000
                      Residuals   65   195,556.02    3,008.55

Conduct a hypothesis test to determine if these data provide convincing evidence that the average weight
of chicks varies across some (or all) groups. Make sure to check relevant conditions. Figures and summary
statistics are shown below.

                                                                            G
        400                                                               G

        350

                                                                                    casein       323.58   64.43   12            grams) 300                                                              Mean   SD    n
                                                                            horsebean   160.20   38.63   10
      (in
        250                                                                          linseed      218.75   52.24   12
                                                                            G          meatmeal   276.91   64.90   11            Weight 200                                                               soybean     246.43   54.13   14
                                                                        sunﬂower    328.92   48.84   12
        150

        100
                     casein  horsebean  linseed  meatmeal  soybean  sunflower


7.38  Teaching descriptive statistics. A study compared ﬁve diﬀerent methods for teaching descriptive
statistics.  The ﬁve methods were traditional lecture and discussion, programmed textbook instruction,
programmed text with lectures, computer instruction, and computer instruction with lectures. 45 students
were randomly assigned, 9 to each method. After completing the course, students took a 1-hour exam.

(a) What are the hypotheses for evaluating if the average test scores are diﬀerent for the diﬀerent teaching
    methods?
(b) What are the degrees of freedom associated with the F-test for evaluating these hypotheses?
(c) Suppose the p-value for this test is 0.0168. What is the conclusion?

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 296

296                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


               7.39  Coffee, depression, and physical activity. Caﬀeine is the world’s most widely used stimulant, with
               approximately 80% consumed in the form of coﬀee. Participants in a study investigating the relationship
              between coﬀee consumption and exercise were asked to report the number of hours they spent per week on
              moderate (e.g., brisk walking) and vigorous (e.g., strenuous sports and jogging) exercise. Based on these
              data the researchers estimated the total hours of metabolic equivalent tasks (MET) per week, a value always
                greater than 0. The table below gives summary statistics of MET for women in this study based on the
             amount of coﬀee consumed.36
                                                Caﬀeinated coﬀee consumption
                 ≤1 cup/week   2-6 cups/week   1 cup/day   2-3 cups/day  ≥4 cups/day    Total
                Mean             18.7             19.6         19.3            18.9            17.5
               SD               21.1             25.5         22.5            22.0            22.0
                  n              12,215            6,617      17,234         12,290           2,383   50,739

                (a) Write the hypotheses for evaluating if the average physical activity level varies among the diﬀerent levels
                      of coﬀee consumption.
                (b) Check conditions and describe any assumptions you must make to proceed with the test.
                 (c) Below is part of the output associated with this test. Fill in the empty cells.

                                              Df    Sum Sq   Mean Sq   F value  Pr(>F)

                                 coﬀee     XXXXX    XXXXX   XXXXX   XXXXX     0.0003

                                   Residuals  XXXXX    25,564,819  XXXXX

                                  Total     XXXXX    25,575,327

                (d) What is the conclusion of the test?

               7.40  Student performance across discussion sections. A professor who teaches a large introductory
                  statistics class (197 students) with eight discussion sections would like to test if student performance diﬀers
             by discussion section, where each discussion section has a diﬀerent teaching assistant. The summary table
              below shows the average ﬁnal exam score for each discussion section as well as the standard deviation of
                scores and the number of students in each section.

                                     Sec 1   Sec 2   Sec 3   Sec 4   Sec 5   Sec 6   Sec 7   Sec 8
                                   ni     33     19     10     29     33     10     32     31
                                                       ¯xi   92.94   91.11   91.80   92.45   89.30   88.30   90.12   93.35
                                          si    4.21    5.58    3.43    5.92    9.32    7.27    6.93    4.57

            The ANOVA output below can be used to test for diﬀerences between the average scores from the diﬀerent
                discussion sections.

                                            Df  Sum Sq  Mean Sq  F value  Pr(>F)
                                         section       7    525.01      75.00      1.87    0.0767
                                      Residuals   189   7584.11      40.13

             Conduct a hypothesis test to determine if these data provide convincing evidence that the average score varies
                across some (or all) groups. Check conditions and describe any assumptions you must make to proceed with
               the test.





                 36M. Lucas et al. “Coﬀee, caﬀeine, and risk of depression among women”. In: Archives of internal medicine 171.17
                  (2011), p. 1571.

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 297

7.5. COMPARING MANY MEANS WITH ANOVA                                                  297


7.41 GPA and major. Undergraduate students taking an introductory statistics course at Duke University
conducted a survey about GPA and major. The side-by-side box plots show the distribution of GPA among
three groups of majors. Also provided is the ANOVA output.

                                    4.0

                                    3.5
                               GPA
                                    3.0

                                    2.5                                                    G
                                          Arts and Humanities   Natural Sciences     Social Sciences


                               Df  Sum Sq  Mean Sq  F value  Pr(>F)
                    major        2      0.03      0.015     0.185    0.8313
                       Residuals   195     15.77      0.081

(a) Write the hypotheses for testing for a diﬀerence between average GPA across majors.
(b) What is the conclusion of the hypothesis test?
(c) How many students answered these questions on the survey, i.e. what is the sample size?

7.42  Work hours and education. The General Social Survey collects data on demographics, education,
and work, among many other characteristics of US residents.37 Using ANOVA, we can consider educational attainment levels for all 1,172 respondents at once. Below are the distributions of hours worked by
educational attainment and relevant summary statistics that will be helpful in carrying out this analysis.

                                        Educational attainment
                        Less than HS   HS   Jr Coll   Bachelor’s   Graduate   Total
            Mean           38.67    39.6    41.39        42.55       40.85   40.45
           SD             15.81   14.97      18.1        13.62       15.51   15.17
             n               121    546       97         253        155   1,172

                    week 80
               per 60

                40                              worked
                         Hours 20
                 0
                         Less than HS       HS               Jr Coll          Bachelor's        Graduate


(a) Write hypotheses for evaluating whether the average number of hours worked varies across the ﬁve
    groups.
(b) Check conditions and describe any assumptions you must make to proceed with the test.
(c) Below is part of the output associated with this test. Fill in the empty cells.

                                 Df   Sum Sq   Mean Sq     F-value  Pr(>F)

                    degree    XXXXX   XXXXX       501.54  XXXXX     0.0682

                    Residuals  XXXXX     267,382  XXXXX

                    Total     XXXXX   XXXXX

(d) What is the conclusion of the test?

7.43  True / False: ANOVA, Part I. Determine if the following statements are true or false in ANOVA, and
explain your reasoning for statements you identify as false.

(a) As the number of groups increases, the modiﬁed signiﬁcance level for pairwise tests increases as well.
(b) As the total sample size increases, the degrees of freedom for the residuals increases as well.
(c) The constant variance condition can be somewhat relaxed when the sample sizes are relatively consistent
    across groups.
(d) The independence assumption can be relaxed when the total sample size is large.

   37National Opinion Research Center, General Social Survey, 2018.

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 298

298                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


               7.44  Child care hours. The China Health and Nutrition Survey aims to examine the eﬀects of the health,
                 nutrition, and family planning policies and programs implemented by national and local governments.38 It,
                  for example, collects information on number of hours Chinese parents spend taking care of their children
              under age 6. The side-by-side box plots below show the distribution of this variable by educational attainment
                 of the parent. Also provided below is the ANOVA output for comparing average hours across educational
               attainment categories.


                   150
                                  hours                   100
                           care
                                  Child 50


                     0
                                Primary school     Lower middle school   Upper middle school   Technical or vocational        College

                                           Df   Sum Sq  Mean Sq  F value  Pr(>F)
                                    education     4     4142.09    1035.52      1.26    0.2846
                                     Residuals   794   653047.83     822.48

                (a) Write the hypotheses for testing for a diﬀerence between the average number of hours spent on child
                    care across educational attainment levels.
                (b) What is the conclusion of the hypothesis test?

               7.45  Prison isolation experiment, Part II. Exercise 7.31 introduced an experiment that was conducted
              with the goal of identifying a treatment that reduces subjects’ psychopathic deviant T scores, where this
                score measures a person’s need for control or his rebellion against control. In Exercise 7.31 you evaluated the
                success of each treatment individually. An alternative analysis involves comparing the success of treatments.
            The relevant ANOVA output is given below.

                                            Df  Sum Sq  Mean Sq  F value  Pr(>F)
                                     treatment    2    639.48     319.74      3.33    0.0461
                                      Residuals   39   3740.43      95.91
                                                                                 spooled = 9.793 on df = 39

                (a) What are the hypotheses?
                (b) What is the conclusion of the test? Use a 5% signiﬁcance level.
                 (c)  If in part (b) you determined that the test is signiﬁcant, conduct pairwise tests to determine which
                  groups are diﬀerent from each other. If you did not reject the null hypothesis in part (b), recheck your
                   answer. Summary statistics for each group are provided below

                                                        Tr 1   Tr 2   Tr 3
                                          Mean   6.21   2.86   -3.21
                                      SD      12.3   7.94    8.57
                                              n        14    14     14


               7.46  True / False: ANOVA, Part II. Determine if the following statements are true or false, and explain
              your reasoning for statements you identify as false.
                            If the null hypothesis that the means of four groups are all the same is rejected using ANOVA at a 5%
                signiﬁcance level, then ...

                (a) we can then conclude that all the means are diﬀerent from one another.
                (b) the standardized variability between groups is higher than the standardized variability within groups.
                 (c) the pairwise analysis will identify at least one pair of means that are signiﬁcantly diﬀerent.
                (d) the appropriate α to be used in pairwise comparisons is 0.05 / 4 = 0.0125 since there are four groups.





              38UNC Carolina Population Center, China Health and Nutrition Survey, 2006.

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 299

7.5. COMPARING MANY MEANS WITH ANOVA                                                  299


Chapter exercises



7.47  Gaming and distracted eating, Part I. A group of researchers are interested in the possible eﬀects of
distracting stimuli during eating, such as an increase or decrease in the amount of food consumption. To test
this hypothesis, they monitored food intake for a group of 44 patients who were randomized into two equal
groups. The treatment group ate lunch while playing solitaire, and the control group ate lunch without any
added distractions. Patients in the treatment group ate 52.1 grams of biscuits, with a standard deviation of
45.1 grams, and patients in the control group ate 27.1 grams of biscuits, with a standard deviation of 26.4
grams. Do these data provide convincing evidence that the average food intake (measured in amount of
biscuits consumed) is diﬀerent for the patients in the treatment group? Assume that conditions for inference
are satisﬁed.39

7.48 Gaming and distracted eating, Part II. The researchers from Exercise 7.47 also investigated the eﬀects
of being distracted by a game on how much people eat. The 22 patients in the treatment group who ate
their lunch while playing solitaire were asked to do a serial-order recall of the food lunch items they ate.
The average number of items recalled by the patients in this group was 4. 9, with a standard deviation of
1.8. The average number of items recalled by the patients in the control group (no distraction) was 6.1, with
a standard deviation of 1.8. Do these data provide strong evidence that the average number of food items
recalled by the patients in the treatment and control groups are diﬀerent?

7.49  Sample size and pairing. Determine if the following statement is true or false, and if false, explain
your reasoning: If comparing means of two groups with equal sample sizes, always use a paired test.

7.50  College credits. A college counselor is interested in estimating how many credits a student typically
enrolls in each semester. The counselor decides to randomly sample 100 students by using the registrar’s
database of students. The histogram below shows the distribution of the number of credits taken by these
students. Sample statistics for this distribution are also provided.

             20                                          Min         8
                                                    Q1         13
             10                                              Median     14                                   Frequency                                            Mean     13.65
              0                                     SD        1.91
                                                    Q3         15
                 8     10    12    14    16    18        Max        18
                         Number of credits

(a) What is the point estimate for the average number of credits taken per semester by students at this
    college? What about the median?
(b) What is the point estimate for the standard deviation of the number of credits taken per semester by
    students at this college? What about the IQR?
(c) Is a load of 16 credits unusually high for this college? What about 18 credits? Explain your reasoning.
(d) The college counselor takes another random sample of 100 students and this time ﬁnds a sample mean
     of 14.02 units. Should she be surprised that this sample statistic is slightly diﬀerent than the one from
    the original sample? Explain your reasoning.
(e) The sample means given above are point estimates for the mean number of credits taken by all students
    at that college. What measures do we use to quantify the variability of this estimate? Compute this
    quantity using the data from the original sample.





   39R.E. Oldham-Cooper et al. “Playing a computer game during lunch aﬀects fullness, memory for lunch, and later
snack intake”. In: The American Journal of Clinical Nutrition 93.2 (2011), p. 308.

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 300

300                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


               7.51 Hen eggs. The distribution of the number of eggs laid by a certain species of hen during their breeding
               period has a mean of 35 eggs with a standard deviation of 18.2. Suppose a group of researchers randomly
              samples 45 hens of this species, counts the number of eggs laid during their breeding period, and records
               the sample mean. They repeat this 1,000 times, and build a distribution of sample means.

                (a) What is this distribution called?
                (b) Would you expect the shape of this distribution to be symmetric, right skewed, or left skewed? Explain
                  your reasoning.
                 (c) Calculate the variability of this distribution and state the appropriate term used to refer to this value.
                (d) Suppose the researchers’ budget is reduced and they are only able to collect random samples of 10 hens.
               The sample mean of the number of eggs is recorded, and we repeat this 1,000 times, and build a new
                     distribution of sample means. How will the variability of this new distribution compare to the variability
                      of the original distribution?

               7.52  Forest management. Forest rangers wanted to better understand the rate of growth for younger trees
                 in the park. They took measurements of a random sample of 50 young trees in 2009 and again measured
               those same trees in 2019. The data below summarize their measurements, where the heights are in feet:

                                                   2009   2019   Diﬀerences
                                                                                    ¯x   12.0   24.5       12.5
                                                   s    3.5     9.5        7.2
                                        n    50     50       50

               Construct a 99% conﬁdence interval for the average growth of (what had been) younger trees in the park
                over 2009-2019.

               7.53  Experiment resizing.  At a startup company running a new weather app, an engineering team
                generally runs experiments where a random sample of 1% of the app’s visitors in the control group and
               another 1% were in the treatment group to test each new feature. The team’s core goal is to increase a
               metric called daily visitors, which is essentially the number of visitors to the app each day. They track
                 this metric in each experiment arm and as their core experiment metric. In their most recent experiment,
               the team tested including a new animation when the app started, and the number of daily visitors in this
              experiment stabilized at +1.2% with a 95% conﬁdence interval of (-0.2%, +2.6%). This means if this new
             app start animation was launched, the team thinks they might lose as many as 0.2% of daily visitors or
               gain as many as 2.6% more daily visitors. Suppose you are consulting as the team’s data scientist, and after
                discussing with the team, you and they agree that they should run another experiment that is bigger. You
                 also agree that this new experiment should be able to detect a gain in the daily visitors metric of 1.0% or
             more with 80% power. Now they turn to you and ask, “How big of an experiment do we need to run to
               ensure we can detect this eﬀect?”

                (a) How small must the standard error be if the team is to be able to detect an eﬀect of 1.0% with 80%
                 power and a signiﬁcance level of α = 0.05? You may safely assume the percent change in daily visitors
                   metric follows a normal distribution.
                (b) Consider the ﬁrst experiment, where the point estimate was +1.2% and the 95% conﬁdence interval was
                    (-0.2%, +2.6%).  If that point estimate followed a normal distribution, what was the standard error of
                   the estimate?
                 (c) The ratio of the standard error from part (a) vs the standard error from part (b) should be 2.03. How
               much bigger of an experiment is needed to shrink a standard error by a factor of 2.03?
                (d) Using your answer from part (c) and that the original experiment was a 1% vs 1% experiment to
                recommend an experiment size to the team.

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 301

7.5. COMPARING MANY MEANS WITH ANOVA                                                  301


7.54  Torque on a rusty bolt.  Project Farm is a YouTube channel that routinely compares diﬀerent
products. In one episode, the channel evaluated diﬀerent options for loosening rusty bolts.40 Eight options
were evaluated, including a control group where no treatment was given (“none” in the graph), to determine
which was most eﬀective. For all treatments, there were four bolts tested, except for a treatment of heat
with a blow torch, where only two data points were collected. The results are shown in the ﬁgure below:


                    Heat
              WD−40
             Royal Purple
            PB Blaster
              Liquid Wrench
                  AeroKroil
             Acetone/ATF
                  none

                               90       100       110       120       130       140

                                   Torque Required to Loosen Rusty Bolt, in Foot−Pounds

(a) Do you think it is reasonable to apply ANOVA in this case?
(b) Regardless of your answer in part (a), describe hypotheses for ANOVA in this context, and use the table
    below to carry out the test. Give your conclusion in the context of the data.

                                Df  Sum Sq  Mean Sq  F value  Pr(>F)
                        treatment    7   3603.43     514.78      4.03    0.0056
                         Residuals   22   2812.80     127.85

(c) The table below are p-values for pairwise t-tests comparing each of the diﬀerent groups. These p-values
    have not been corrected for multiple comparisons. Which pair of groups appears most likely to represent
    a diﬀerence?

                        AeroKroil   Heat    Liquid Wrench   none   PB Blaster   Royal Purple  WD-40
      Acetone/ATF      0.2026     0.0308       0.0476       0.1542     0.3294        0.5222       0.3744
       AeroKroil                    0.0027       0.0025       0.8723     0.7551        0.5143       0.6883
       Heat                                      0.5580       0.0020     0.0050        0.0096       0.0059
       Liquid Wrench                                         0.0017     0.0053        0.0117       0.0065
       none                                                              0.6371        0.4180       0.5751
     PB Blaster                                                                       0.7318       0.9286
       Royal Purple                                                                                 0.8000

(d) There are 28 p-values shown in the table in part (c). Determine if any of them are statistically signiﬁcant
     after correcting for multiple comparisons. If so, which one(s)? Explain your answer.

7.55  Exclusive relationships. A survey conducted on a reasonably random sample of 203 undergraduates
asked, among many other questions, about the number of exclusive relationships these students have been
in. The histogram below shows the distribution of the data from this sample. The sample average is 3.2
with a standard deviation of 1.97.

                      100

                       80

                       60

                       40

                       20

                        0
                            0          2          4          6          8         10
                      Number of exclusive relationships

Estimate the average number of exclusive relationships Duke students have been in using a 90% conﬁdence
interval and interpret this interval in context. Check any conditions required for inference, and note any
assumptions you must make as you proceed with your calculations and conclusions.

   40Project Farm on YouTube, youtu.be/xUEob2oAKVs, April 16, 2018.

---

# OpenIntro Statistics, 4th edition

## 7.5 — Comparing many means with ANOVA

### PDF page 302

302                                CHAPTER 7. INFERENCE FOR NUMERICAL DATA


               7.56  Age at ﬁrst marriage, Part I. The National Survey of Family Growth conducted by the Centers
                  for Disease Control gathers information on family life, marriage and divorce, pregnancy, infertility, use of
                contraception, and men’s and women’s health. One of the variables collected on this survey is the age at
                ﬁrst marriage. The histogram below shows the distribution of ages at ﬁrst marriage of 5,534 randomly
              sampled women between 2006 and 2010. The average age at ﬁrst marriage among these women is 23.44 with
              a standard deviation of 4.72.41

                                      1000

                                       800

                                       600

                                       400

                                       200

                                         0
                                             10      15      20      25      30      35      40      45
                                      Age at first marriage

              Estimate the average age at ﬁrst marriage of women using a 95% conﬁdence interval, and interpret this
                 interval in context. Discuss any relevant assumptions.

               7.57  Online communication. A study suggests that the average college student spends 10 hours per week
              communicating with others online. You believe that this is an underestimate and decide to collect your own
              sample for a hypothesis test. You randomly sample 60 students from your dorm and ﬁnd that on average
               they spent 13.5 hours a week communicating with others online. A friend of yours, who oﬀers to help you
              with the hypothesis test, comes up with the following set of hypotheses. Indicate any errors you see.

                                           H0 : ¯x < 10 hours
                                    HA : ¯x > 13.5 hours

               7.58  Age at ﬁrst marriage, Part II. Exercise 7.56 presents the results of a 2006 - 2010 survey showing that
               the average age of women at ﬁrst marriage is 23.44. Suppose a social scientist thinks this value has changed
                 since the survey was taken. Below is how she set up her hypotheses. Indicate any errors you see.

                                         H0 : ¯x̸ = 23.44 years old
                                   HA : ¯x = 23.44 years old





                   41Centers for Disease Control and Prevention, National Survey of Family Growth, 2010.

---

# OpenIntro Statistics, 4th edition

## 8.1 — Fitting a line, residuals, and correlation

### PDF page 303

303

Chapter 8

Introduction to linear
regression





8.1 Fitting a line, residuals, and correlation

8.2 Least squares regression

8.3 Types of outliers in linear regression

8.4 Inference for linear regression

---

# OpenIntro Statistics, 4th edition

## 8.1 — Fitting a line, residuals, and correlation

### PDF page 304

304





          Linear regression is a very powerful statistical technique. Many people

         have some familiarity with regression just from reading the news, where

           straight lines are overlaid on scatterplots. Linear models can be used for

           prediction or to evaluate whether there is a linear relationship between

         two numerical variables.





         For videos, slides, and other resources, please visit
        www.openintro.org/os

---

# OpenIntro Statistics, 4th edition

## 8.1 — Fitting a line, residuals, and correlation

### PDF page 305

8.1. FITTING A LINE, RESIDUALS, AND CORRELATION                                         305


8.1  Fitting a line, residuals, and correlation



      It’s helpful to think deeply about the line ﬁtting process. In this section, we deﬁne the form
of a linear model, explore criteria for what makes a good ﬁt, and introduce a new statistic called
correlation.


8.1.1  Fitting a line to data

     Figure 8.1 shows two variables whose relationship can be modeled perfectly with a straight line.
The equation for the line is

                                    y = 5 + 64.96x

Consider what a perfect linear relationship means: we know the exact value of y just by knowing the
value of x. This is unrealistic in almost any natural process. For example, if we took family income
(x), this value would provide some useful information about how much ﬁnancial support a college
may oﬀer a prospective student (y). However, the prediction would be far from perfect, since other
factors play a role in ﬁnancial support beyond a family’s ﬁnances.


                     $2k                                   G G
                                                         G                                                     Purchase
                                                  G
                                                 G

                                              G                                 Share
                     $1k                  G                    the                    G
             of


                              G                           Cost          G   G

                          G                                 Total   $0
                         0          10         20         30
                      Number of Target Corporation Stocks to Purchase

        Figure 8.1: Requests from twelve separate buyers were simultaneously placed with
        a trading company to purchase Target Corporation stock (ticker TGT, December
         28th, 2018), and the total cost of the shares were reported. Because the cost is
       computed using a linear formula, the linear ﬁt is perfect.


     Linear regression is the statistical method for ﬁtting a line to data where the relationship
between two variables, x and y, can be modeled by a straight line with some error:

                                     y = β0 + β1x + ε

The values β0 and β1 represent the model’s parameters (β is the Greek letter beta), and the error is
represented by ε (the Greek letter epsilon). The parameters are estimated using data, and we write
their point estimates as b0 and b1. When we use x to predict y, we usually call x the explanatory or
predictor variable, and we call y the response; we also often drop the ϵ term when writing down
the model since our main focus is often on the prediction of the average outcome.
      It is rare for all of the data to fall perfectly on a straight line. Instead, it’s more common for
data to appear as a cloud of points, such as those examples shown in Figure 8.2. In each case, the
data fall around a straight line, even if none of the observations fall exactly on the line. The ﬁrst
plot shows a relatively strong downward linear trend, where the remaining variability in the data
around the line is minor relative to the strength of the relationship between x and y. The second
plot shows an upward trend that, while evident, is not as strong as the ﬁrst. The last plot shows a

---

# OpenIntro Statistics, 4th edition

## 8.1 — Fitting a line, residuals, and correlation

### PDF page 306

306                            CHAPTER 8. INTRODUCTION TO LINEAR REGRESSION


                                                                               400
               50
                                             20000
                                                                               200

                0                            10000
                                                                                 0


                                                 0              −50                                                            −200
                    −50       0       50          500     1000     1500                 0      20     40

                      Figure 8.2: Three data sets where a linear model may be useful even though the
                     data do not all fall exactly on the line.


                           15                                   G  G  G  G  G
                                                                        G                 G                          (m)                                   G                                                                                              G
                                                                  G                              G
                           10                    G  G                                    G  G
                                                         G     Best fitting straight line is flat (!)      G                                                                      Traveled
                            5           G  G                                                      G  G

                                                G                                                                  G

                                             G                                                                        G                                                                      Distance   0

                                0                30               60               90
                                                    Angle of Incline (Degrees)

                      Figure 8.3: A linear model is not useful in this nonlinear case. These data are from
                    an introductory physics experiment.


              very weak downward trend in the data, so slight we can hardly notice it. In each of these examples,
           we will have some uncertainty regarding our estimates of the model parameters, β0 and β1. For
               instance, we might wonder, should we move the line up or down a little, or should we tilt it more
               or less? As we move forward in this chapter, we will learn about criteria for line-ﬁtting, and we will
                also learn about the uncertainty associated with estimates of model parameters.
                 There are also cases where ﬁtting a straight line to the data, even if there is a clear relationship
             between the variables, is not helpful. One such case is shown in Figure 8.3 where there is a very clear
               relationship between the variables even though the trend is not linear. We discuss nonlinear trends
                in this chapter and the next, but details of ﬁtting nonlinear models are saved for a later course.


            8.1.2  Using linear regression to predict possum head lengths

                   Brushtail possums are a marsupial that lives in Australia, and a photo of one is shown in
              Figure 8.4. Researchers captured 104 of these animals and took body measurements before releasing
              the animals back into the wild. We consider two of these measurements: the total length of each
             possum, from head to tail, and the length of each possum’s head.
                  Figure 8.5 shows a scatterplot for the head length and total length of the possums.  Each
              point represents a single possum from the data. The head and total length variables are associated:
            possums with an above average total length also tend to have above average head lengths. While the
               relationship is not perfectly linear, it could be helpful to partially explain the connection between
               these variables with a straight line.

---

# OpenIntro Statistics, 4th edition

## 8.1 — Fitting a line, residuals, and correlation

### PDF page 307

8.1. FITTING A LINE, RESIDUALS, AND CORRELATION                                         307





               Figure 8.4: The common brushtail possum of Australia.
       —————————–
               Photo by Greg Schechter (https://ﬂic.kr/p/9BAFbR). CC BY 2.0 license.




               100

                 (mm)                95
                          Length                           G
                 Head  90

                85


                    75          80          85          90          95

                                                    Total Length (cm)

        Figure 8.5: A scatterplot showing head length against total length for 104 brushtail
        possums. A point representing a possum with head length 94.1mm and total length
       89cm is highlighted.


   We want to describe the relationship between the head length and total length variables in the
possum data set using a line. In this example, we will use the total length as the predictor variable,
x, to predict a possum’s head length, y. We could ﬁt the linear relationship by eye, as in Figure 8.6.
The equation for this line is

                                                                 ˆy = 41 + 0.59x

A “hat” on y is used to signify that this is an estimate. We can use this line to discuss properties
of possums. For instance, the equation predicts a possum with a total length of 80 cm will have a
head length of

                                                              ˆy = 41 + 0.59 × 80

                        = 88.2

The estimate may be viewed as an average: the equation predicts that possums with a total length
of 80 cm will have an average head length of 88.2 mm. Absent further information about an 80 cm
possum, the prediction for head length that uses the average is a reasonable estimate.

---

# OpenIntro Statistics, 4th edition

## 8.1 — Fitting a line, residuals, and correlation

### PDF page 308

308                            CHAPTER 8. INTRODUCTION TO LINEAR REGRESSION



                            100
                                          (mm)
                             95
                                                               Length
                             90
                                          Head
                             85


                                 75         80         85         90         95
                                                                   Total Length (cm)

                      Figure 8.6: A reasonable linear model was ﬁt to represent the relationship between
                    head length and total length.



          EXAMPLE 8.1
           What other variables might help us predict the head length of a possum besides its length?

             Perhaps the relationship would be a little diﬀerent for male possums than female possums, or perhaps
                   it would diﬀer for possums from one region of Australia versus another region. In Chapter 9, we’ll
               learn about how we can include more than one predictor. Before we get there, we ﬁrst need to better
             understand how to best build a simple linear model with one predictor.



            8.1.3  Residuals

            Residuals are the leftover variation in the data after accounting for the model ﬁt:

                                           Data = Fit + Residual

            Each observation will have a residual, and three of the residuals for the linear model we ﬁt for the
            possum data is shown in Figure 8.6. If an observation is above the regression line, then its residual,
              the vertical distance from the observation to the line, is positive. Observations below the line have
              negative residuals. One goal in picking the right linear model is for these residuals to be as small as
                possible.
                    Let’s look closer at the three residuals featured in Figure 8.6. The observation marked by an
           “×” has a small, negative residual of about -1; the observation marked by “+” has a large residual
                of about +7; and the observation marked by “△” has a moderate residual of about -4. The size of
             a residual is usually discussed in terms of its absolute value. For example, the residual for “△” is
                larger than that of “×” because | −4| is larger than | −1|.


              RESIDUAL: DIFFERENCE BETWEEN OBSERVED AND EXPECTED
             The residual of the ith observation (xi, yi) is the diﬀerence of the observed response (yi) and
                the response we would predict based on the model ﬁt (ˆyi):

                                                                  ei = yi −ˆyi

           We typically identify ˆyi by plugging xi into the model.

---

# OpenIntro Statistics, 4th edition

## 8.1 — Fitting a line, residuals, and correlation

### PDF page 309

8.1. FITTING A LINE, RESIDUALS, AND CORRELATION                                         309



EXAMPLE 8.2
The linear ﬁt shown in Figure 8.6 is given as ˆy = 41 + 0.59x. Based on this line, formally compute
the residual of the observation (77.0, 85.3). This observation is denoted by “×” in Figure 8.6. Check
it against the earlier visual estimate, -1.

We ﬁrst compute the predicted value of point “×” based on the model:

                              ˆy× = 41 + 0.59x× = 41 + 0.59 × 77.0 = 86.4

Next we compute the diﬀerence of the actual head length and the predicted head length:

                        e× = y× −ˆy× = 85.3 −86.4 = −1.1

The model’s error is e× = −1.1mm, which is very close to the visual estimate of -1mm. The negative
residual indicates that the linear model overpredicted head length for this particular possum.


GUIDED PRACTICE 8.3
If a model underestimates an observation, will the residual be positive or negative? What about if
it overestimates the observation?1



GUIDED PRACTICE 8.4
Compute the residuals for the “+” observation (85.0, 98.6) and the “△” observation (95.5, 94.0) in
the ﬁgure using the linear relationship ˆy = 41 + 0.59x.2


     Residuals are helpful in evaluating how well a linear model ﬁts a data set. We often display
them in a residual plot such as the one shown in Figure 8.7 for the regression line in Figure 8.6.
The residuals are plotted at their original horizontal locations but with the vertical coordinate as
the residual. For instance, the point (85.0, 98.6)+ had a residual of 7.45, so in the residual plot it
is placed at (85.0, 7.45). Creating a residual plot is sort of like tipping the scatterplot over so the
regression line is horizontal.



                 5


                 0                                               Residuals

               −5

                    75         80         85         90         95
                                                  Total Length (cm)

                     Figure 8.7: Residual plot for the model in Figure 8.6.



    1If a model underestimates an observation, then the model estimate is below the actual. The residual, which is
the actual observation value minus the model estimate, must then be positive. The opposite is true when the model
overestimates the observation: the residual is negative.
   2(+) First compute the predicted value based on the model:

                                         ˆy+ = 41 + 0.59x+ = 41 + 0.59 × 85.0 = 91.15

Then the residual is given by

                               e+ = y+ −ˆy+ = 98.6 −91.15 = 7.45

This was close to the earlier estimate of 7.
(△) ˆy△= 41 + 0.59x△= 97.3. e△= y△−ˆy△= −3.3, close to the estimate of -4.

---

# OpenIntro Statistics, 4th edition

## 8.1 — Fitting a line, residuals, and correlation

### PDF page 310

310                            CHAPTER 8. INTRODUCTION TO LINEAR REGRESSION





                      Figure 8.8: Sample data with their best ﬁtting lines (top row) and their corre-
                     sponding residual plots (bottom row).



          EXAMPLE 8.5
           One purpose of residual plots is to identify characteristics or patterns still apparent in data after
               ﬁtting a model. Figure 8.8 shows three scatterplots with linear models in the ﬁrst row and residual
               plots in the second row. Can you identify any patterns remaining in the residuals?

              In the ﬁrst data set (ﬁrst column), the residuals show no obvious patterns. The residuals appear to
             be scattered randomly around the dashed line that represents 0.

           The second data set shows a pattern in the residuals. There is some curvature in the scatterplot,
             which is more obvious in the residual plot. We should not use a straight line to model these data.
               Instead, a more advanced technique should be used.

           The last plot shows very little upwards trend, and the residuals also show no obvious patterns. It is
              reasonable to try to ﬁt a linear model to the data. However, it is unclear whether there is statistically
               signiﬁcant evidence that the slope parameter is diﬀerent from zero. The point estimate of the slope
              parameter, labeled b1, is not zero, but we might wonder if this could just be due to chance. We will
              address this sort of scenario in Section 8.4.




            8.1.4  Describing linear relationships with correlation

            We’ve seen plots with strong linear relationships and others with very weak linear relationships. It
             would be useful if we could quantify the strength of these linear relationships with a statistic.


             CORRELATION: STRENGTH OF A LINEAR RELATIONSHIP
               Correlation, which always takes values between -1 and 1, describes the strength of the linear
                  relationship between two variables. We denote the correlation by R.


            We can compute the correlation using a formula, just as we did with the sample mean and stan-
             dard deviation. This formula is rather complex,3 and like with other statistics, we generally perform

                    3Formally, we can compute the correlation for observations (x1, y1), (x2, y2), ..., (xn, yn) using the formula

                                                            1                                                           n  xi −¯x yi −¯y                      X                                    R =
                                                n −1                                                                    i=1  sx    sy

               where ¯x, ¯y, sx, and sy are the sample means and standard deviations for each variable.