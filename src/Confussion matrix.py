#importing matplotlib for plotting graph
import matplotlib.pyplot as plt


#calculate the TPR - true positive rate: 
def calTPR(TP,FN):
    #declaring variables
    TPR = 0
    TPR_col = []
    #iterating over each value of the TP and FN list
    
    for i in range (0,len(TP)):
        '''  TP
           ------ = TPR
           TP + FN
        '''   
        TPR = TP[i] / (TP[i] + FN[i])
        #adding the values in the TPR_col
        TPR_col.append(TPR)
        
    return TPR_col

#calculate the FPR - false positive rate
def calFPR(FP,TN):
    #declaring variables
    FPR = 0
    FPR_col = []
    
    #iterating over each value of the TP and FN list
    for i in range (0,len(FP)):
        '''  FP
           ------ = FPR
           TN + FP
        '''   
        FPR = FP[i] / (TN[i] + FP[i])
        #adding the values in the TPR_col
        FPR_col.append(FPR)
        
    return FPR_col

#plotting the graph using fpr and tpr values
def plot_roc_curve(FPR, TPR): #two parameters
    #setting color for tpr and fpr
    plt.plot(FPR, TPR, color='orange', label='ROC')
    #setting the style 
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    #naming the label and titles
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    #plot the  graph and show
    plt.legend()
    plt.show()


#finding the accurate
def calACC(TP, FP, FN, TN):
    #declaring varaibles
    ACC = 0
    ACC_col = []

    #iterating over each value
    for i in range (0,10):
        '''    TP + TN          
           ----------------- = ACC
           TP + TN + FN + FP
        '''
        ACC = (TP[i] + TN[i]) / (TP[i] + TN[i] + FN[i] + FP[i])
        #adding values in ACC
        ACC_col.append(ACC)

        return max(ACC_col)

#declaring the list

#true positive
TP = [10, 9, 8, 8, 6, 5, 5, 4, 3, 3, 1, 0]
#false positive
FP = [10, 10, 9, 8, 8, 8, 6, 6, 5, 2, 2, 0]
#false negative
FN = [0, 1, 2, 2, 4, 5, 5, 6, 7, 7, 9, 10]
#true negative
TN = [0, 0, 1, 2, 2, 2, 4, 4, 5, 8, 8, 10]

#calling all the functions
print(calTPR(TP,FN))
print(calFPR(FP,TN))
print("Maximum value of Accuracy is: ", calACC(TP, FP, FN, TN))
plot_roc_curve(calFPR(FP,TN),calTPR(TP,FN))
