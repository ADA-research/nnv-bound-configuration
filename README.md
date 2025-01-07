#Automated Design of Linear Bounding Functions for Sigmoidal Nonlinearities in Neural Networks

This is the accompanying repository to the paper:

**Automated Design of Linear Bounding Functions for Sigmoidal Nonlinearities in Neural Networks**

Matthias König, Xiyue Zhang, Holger H. Hoos, Marta Kwiatkowska & Jan N. van Rijn 

**Abstract:**

The ubiquity of deep learning algorithms in various applications has amplified the need for assuring their robustness against small input perturbations such as those occurring in adversarial attacks. Existing complete verification techniques offer provable guarantees for all robustness queries but struggle to scale beyond small neural networks. To overcome this computational intractability, incomplete verification methods often rely on convex relaxation to over-approximate the nonlinearities in neural networks. 

Progress in tighter approximations has been achieved for piecewise linear functions. However, robustness verification of neural networks for general activation functions (e.g., Sigmoid, Tanh) remains under-explored and poses new challenges. Typically, these networks are verified using convex relaxation techniques, which involve computing linear upper and lower bounds of the nonlinear activation functions.

In this work, we propose a novel parameter search method to improve the quality of these linear approximations. Specifically, we show that using a simple search method, carefully adapted to the given verification problem through state-of-the-art algorithm configuration techniques, improves the average global lower bound by 25% on average over the current state of the art on several commonly used local robustness verification benchmarks.


**Citation:**
```
@inproceedings{
    author = {K{\"o}nig, Matthias and Zhang, Xiyue and Hoos, Holger H and Kwiatkowska, Marta and van Rijn, Jan N},
    title = "{Automated Design of Linear Bounding Functions for Sigmoidal Nonlinearities in Neural Networks}",
    booktitle = "Proceedings of the European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases",
    year = "2024"
}
```

##Example

First, setup the dependencies:

1. Create conda environment
2. Install needed dependencies using ```conda env create -f environment.yml```
3. Now, you can run alpha-beta-CROWN with automated bound configuration using ```python abcrown.py --config exp_configs/cifar_conv_small_tanh-1.yaml --bound_prop_method crown --no_alpha```

This example configures the linear bounds for Tanh-based ConvMed network with epsilon=0.0157 on the first CIFAR-10 instance. During configuration, SMAC performs 200 trials.

To change the network and/or instance, you need to change the config file and/or the instance index in ```arguments.py```.
