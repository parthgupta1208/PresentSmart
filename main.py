import pdf2final_list
import text2ppt

x=pdf2final_list.process(["Logistic Regression","Estimating Probabilities in ML", "Training and cost function in ML", "Decision boundaries in ML", "SoftMax regression", "Non-linear SVM classification","Polynomial kernel in SVM", "adding similarity feature in SVM", "Gaussian RBF Kernel in SVM", "SVM Regression"])
text2ppt.presentate(x)
