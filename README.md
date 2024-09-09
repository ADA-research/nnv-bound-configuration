**Automated Design of Linear Bounding Functions for Sigmoidal Nonlinearities in Neural Networks**

Matthias König, Xiyue Zhang, Holger Hoos, Marta Kwiatkowska, Jan van Rijn

This reposetory contains the code to run alpha-beta-CROWN with automated bound configuration. The following files have been modified:

1. complete_verifier/abcrown.py

The SMAC wrapper is implemented in main.py, so when calling abcrown.py, we start the configuration procedure.
In main.py there is the target function called target_func(), which takes a configuration from SMAC as arguments (among others).
The configurable hyper-parameters are called hp1, hp2, hp3 and hp4, where hp3 and hp4 are conceptually similar to hp1 and hp2 but we are used for lower bound computation (vs. upper bound).

These hyper-parameters are passed into the incomplete_verifier() function.
Within this function, the hyper-parameters are passed onto the LiRPAConvNet class.

2. complete_verifier/beta_CROWN_solver.py

LiRPAConvNet:

Within this class, the network is converted to a BoundedModule. Here, we set the hyper-parameters in the bound_opts dict.

3. auto-LiRPA/operators/activation.py 

BoundSigmoid(BoundTanh):

In this class we call the precompute_relaxation function, which takes our hyper-parameters as arguments.

precompute_relaxation():

Here, upper and lower bounds are computed here, where the function is called per activation layer (referred to as ‘name’).

*Running alpha-beta-CROWN with automated bound configuration using on the cifar_conv_small_sigmoid benchmark*

1. Clone repository

<git clone --recursive https://github.com/ADA-research/nnv-bound-configuration.git>

2. Install SMAC

<pip install SMAC>

3. Start configuration procedure

<cd complete_verifier
python abcrown.py --config exp_configs/beta_crown/cifar_conv_small_sigmoid.yaml>
