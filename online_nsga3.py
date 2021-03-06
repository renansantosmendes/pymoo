import time
from sklearn.cluster import AgglomerativeClustering

from pymoo.algorithms.experiment_online_cluster_nsga3 import ExperimentOnlineClusterNSGA3
from pymoo.algorithms.experiment_nsga3 import ExperimentNSGA3
from pymoo.algorithms.adapted_nsga3 import NSGA3
from pymoo.algorithms.online_cluster_nsga3 import OnlineClusterNSGA3
from pymoo.factory import get_problem, get_reference_directions
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter

# create the reference directions to be used for the optimization
original_dimension = 5
reduced_dimension = 2
interval_of_aggregations = 1
save_data = True
termination_criterion = ('n_gen', 100)
problem = get_problem("dtlz2", n_obj=original_dimension)
number_of_executions = 3
reference_directions = get_reference_directions("das-dennis", original_dimension, n_partitions=12)


# create the algorithm object
# print(algorithm.generate_max_min(problem))

start = time.time()

# execute the optimization
# res = minimize(get_problem("dtlz2", n_obj=original_dimension),
#                algorithm,
#                seed=5,
#                verbose=False,
#                termination=('n_gen', 200))


experiment = ExperimentOnlineClusterNSGA3(ref_dirs=reference_directions,
    pop_size=92,
    cluster=AgglomerativeClustering,
    save_dir='.\\experiment_results\\OnlineClusterNSGA3_{}_{}_{}_{}'.format(problem.name(), original_dimension, reduced_dimension, interval_of_aggregations),
    save_data=True,
    number_of_clusters=reduced_dimension,
    interval_of_aggregations=interval_of_aggregations,
    problem=problem,
    number_of_executions=number_of_executions,
    termination=termination_criterion,
    verbose=False,
    save_history=True,
    use_different_seeds=True)

print('Experiment run')
# experiment.run()
# experiment.show_mean_convergence('hv_convergence.txt')
# experiment.show_mean_convergence('igd_convergence.txt')
# experiment.show_heat_map()


experiment = ExperimentNSGA3(ref_dirs=reference_directions,
    pop_size=92,
    cluster=AgglomerativeClustering,
    save_dir='.\\experiment_results\\NSGA3_{}_{}'.format(problem.name(), original_dimension),
    save_data=True,
    number_of_clusters=reduced_dimension,
    interval_of_aggregations=interval_of_aggregations,
    problem=problem,
    number_of_executions=number_of_executions,
    termination=termination_criterion,
    verbose=False,
    save_history=True,
    use_different_seeds=True)

print('Experiment run')
# experiment.run()
# experiment.show_mean_convergence('hv_convergence.txt')
# experiment.show_mean_convergence('igd_convergence.txt')

algorithm = NSGA3(
            ref_dirs=reference_directions,
            seed=1,
            current_execution_number=0,
            save_dir='.\\experiment_results\\NSGA3_{}_{}'.format(problem.name(), original_dimension),
            save_data=True)

res = minimize(problem,
        algorithm,
        termination=termination_criterion,
        verbose=True,
        save_history=False)

end = time.time()
print('Elapsed Time in experiment', end - start)