# Case Study

In the tutorials we have explored different steps which would commonly be encountered when developing techniques for cuffless blood pressure estimation.

For the remainder of the workshop we would like you to work together in groups to train and test a model for estimating BP from the PPG.

Forming groups:
- Please could any coders spread themselves between groups
- We recommend groups of between 4 and 6 people

A suggested workflow is provided below - feel free to use this or ignore it!

We will be on hand to help, and we will ask groups to share their experiences shortly before the end of the session.

# Suggested workflow

I would suggest the following:
1. Loop through ICU stays, determining whether each stay meets the inclusion criteria for the study (contains at least 10 minutes of simultaneous PPG and ABP signals). The [Data Visualisation tutorial](https://wfdb.io/mimic_wfdb_tutorials/tutorial/notebooks/data-visualisation.html) provides scripts for doing this (except that it only runs on a specified ICU stay, and doesn't loop through stays). Continue looping until 60 ICU stays have been identified which meet
2. Extract 10 minutes of simultaneous PPG and ABP signals from each ICU stay which meets the inclusion criteria.
3. Run signal processing scripts to extract a parameter from the shape of each PPG pulse wave (let's call the parameter the stiffness index - SI). This will produce a vector of values for each ICU stay (with a length of approximately 600 - i.e. one value per heart beat - which varies from one stay to the next), and a vector of corresponding time stamps.
4. Run signal processing scripts to extract systolic and diastolic blood pressure (SBP and DBP) values from each ABP pulse wave. Similarly, this will produce two vectors of values for each ICU stay, one for systolic blood pressure, and one for diastolic blood pressure, and a vector of corresponding time stamps.
5. Calculate an average (e.g. median) value of the SI for each 30 second window, and repeat for SBP and DBP, ensuring that the same timings are used for the SI, SBP and DBP windows. For each ICU stay, this will produce three vectors each of length 20 (because the 10 minute segments can be split into 20 non-overlapping 30-second windows). The three vectors will contain SI, SBP and DBP respectively.
6. Create 'overall' vectors by concatenating each of the three vectors across all ICU stays. This will generate three vectors each of length 1200 (i.e. 20 values for 60 ICU stays). In addition, create a vector of ICU stays (i.e. a vector of length 1200 which contains the ICU stay ID from which each window was obtained).
7. Split the data into training and testing data, at the ICU stay level. E.g. the first 600 values (corresponding to the first 30 ICU stays) are designated as training data, and the remaining 600 values are designated as testing data.
8. Train a linear regression model on the training data to estimate either SBP (or DBP) from SI. The default behaviour should be to use SBP, but it would be nice to include the option to change this to DBP.
9. Test the performance of the model on the testing data:
   - Use the model to estimate SBP (or DBP) from each SI value in the testing data. This should produce a vector of estimated SBP (or DBP) values of length 600.
   - Calculate the errors between the estimated and reference SBP (or DBP) values (using error = estimated - reference).
   - Calculate error statistics for the entire testing dataset. e.g. mean absolute error, bias (i.e. mean error), limits of agreement (i.e. 1.96 * standard deviation of errors).
