import argparse

def common_argparser():

    parser = argparse.ArgumentParser()

    parser.add_argument('--no_solve_slope', action='store_false', dest='solve_slope', help='do not optimize slope/alpha in compute bounds')
    parser.add_argument("--load", type=str, default=None, help='Load pretrained model')
    parser.add_argument("--device", type=str, default="cuda", choices=["cpu", "cuda"], help='use cpu or cuda')
    parser.add_argument("--seed", type=int, default=100, help='random seed')
    parser.add_argument("--norm", type=float, default='inf', help='p norm for epsilon perturbation')
    parser.add_argument("--batch_size", type=int, default=64, help='batch size')
    parser.add_argument('--no_warm', action='store_true', default=False, help='using warm up for lp solver, true by default')
    parser.add_argument('--no_beta', action='store_true', default=False, help='using beta splits, true by default')
    parser.add_argument("--max_subproblems_list", type=int, default=200000, help='max length of sub-problems list')
    parser.add_argument("--decision_thresh", type=float, default=0, help='decision threshold of lower bounds')
    parser.add_argument("--timeout", type=float, default=360, help='timeout for one property')
    parser.add_argument("--start", type=int, default=0, help='start from i-th property')
    parser.add_argument("--end", type=int, default=1000, help='end with (i-1)-th property')
    parser.add_argument("--new_branching", action='store_true', help='try the new gradient based branching heuristic')
    parser.add_argument("--branching_method", default="kfsb", choices=["babsr", "fsb", "kfsb"], help='branching method')
    parser.add_argument("--branching_candidates", type=int, default=3, help='select topK candidate per layer when using fsb or kfsb')
    parser.add_argument("--branching_reduceop", choices=["min", "max", "mean", "auto"], default="min", help='reduction operation to compute branching scores from two sides of a branch.')
    parser.add_argument("--lr_init_alpha", type=float, default=0.1, help='learning rate for relu slopes/alpha at initial')
    parser.add_argument('--init_iteration', type=int, default=100, help='number of iterations for optimized incomplete verifier and initial bounds for BaB verifier')
    parser.add_argument("--lr_alpha", type=float, default=0.01, help='learning rate for relu slopes/alpha')
    parser.add_argument("--lr_beta", type=float, default=0.05, help='learning rate for beta')
    parser.add_argument("--lr_decay", type=float, default=0.98, help='learning rate decay in scheduler')
    parser.add_argument("--optimizer", default="adam", help='optimizer')
    parser.add_argument("--iteration", type=int, default=50, help='iteration of optimization bounds')
    parser.add_argument('--no_beta_warmup', action='store_false', dest='beta_warmup', help='do not use beta warmup from branching history')
    parser.add_argument('--opt_coeffs', action='store_true', dest='opt_coeffs', help='optimize coeffs in compute bounds')
    parser.add_argument('--opt_bias', action='store_true', dest='opt_bias', help='optimize constraint bias in compute bounds')
    parser.add_argument('--opt_intermediate_beta', action='store_true', dest='opt_intermediate_beta', help='optimize constraint bias in compute bounds')
    parser.add_argument('--intermediate_refinement_layers', nargs='+', type=int, default=[-1], help='layers to be refined, separted by commas. -1 means preactivation before last relu.')
    parser.add_argument("--conv_mode", default="patches", choices=["patches", "matrix"], help='conv mode in BoundedModule')
    parser.add_argument("--deterministic", action='store_true', help='Run code in CUDA deterministic mode, slower performance but better reproducibility.')
    parser.add_argument("--double_fp", action='store_true', help='Use double precision floating point. GPUs with good double precision support are needed (NVIDIA P100, V100, A100; AMD Radeon Instinc MI50, MI100)')
    parser.add_argument("--no_per_neuron_slopes", action='store_false', dest='per_neuron_slopes', help='Use per-neuron slope for optimized CROWN bounds.')
    parser.add_argument("--share_slopes", action='store_true', help='When --per_neuron_alpha is True, use shared alpha.')
    parser.add_argument("--loss_reduction_func", default="sum")

    return parser

