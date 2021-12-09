## Saudi Central Bank Treasury Bill Prediction

The project aims to find what drives treasury bill yields. Factors such as inflation and interest rate could have a relation with treasury bill returns.



At first, I used a heatmap to find correlations between variables. 

The response variables of maturity terms show multicollinarity execluding our target variable (52nd week) so we had to get rid of them.


![download](https://user-images.githubusercontent.com/49822946/145378546-3147377d-ee89-42a5-b7bc-5699d2bfb199.png)


Plotting our linear model yields this result

![download](https://user-images.githubusercontent.com/49822946/145397361-c5638256-774e-4a20-8e9b-5a92c1407ca9.png)

The target variable is is showing weird positioning. Spliting the y into two different scenarios might help us.

Other models have been developed; the likes of Ridge model and polynomial. Polynomial with degree 2 yields the best results after implementing kfold with 10 splits and shuffling enabled.

Therefore, our choice of model is Polynomial with degree of 2.





