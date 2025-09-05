# Machine Learning Potential Training Workflow: Data Preparation from AIMD (Phase1)

This workflow outlines the fundamental steps to generate training datasets for machine-learned interatomic potentials (MLIPs) from AIMD. The pipeline focuses on creating diverse and representative atomic configurations with accurate quantum mechanical reference data.

## Workflow Overview

1. **Low accuracy ab Initio Molecular Dynamics (AIMD) Simulation**  
   Initial atomic trajectories are generated using first-principles molecular dynamics to capture realistic thermal fluctuations and structural variations of the target system under specified thermodynamic conditions.
   - **VASP input file can refer the input_aimd folder.**

3. **Structure Sampling**  
   Representative configurations are systematically extracted from AIMD trajectories through time-interval or geometry-based sampling, balancing data diversity with computational efficiency.**The extract structure script is in the extrace-aimd-script folder, the steps to use it are:
   - **Extract the structure under all frame counts from OUTCAR to NEP-dataset.xyz (sh aimd2xyz.sh).**
   - **Extract the structure to train1.xyz every n steps (python mdsimplify. py n).**

5. **Structural Perturbation for Sampled structures from AIMD**  
 Since the NPT of AIMD cannot be applied to a certain direction, NVT has to be used for 2D and 1D structures containing a vacuum layer, however, the lattice is not changed by the NVT process. Therefore the method of perturbing the lattice (±6%) is used to expand the richness of the training set.
   - **Convert all structures in train1.xyz into n POSCAR-n (python xyz2poscar.py).**
   - **Do (±6%) lattice perturbation on POSCAR-n, the perturbation ratio can be set in the script, and generate 50 folders containing structures before and after perturbation for easy comparison (python preturbed-NVT.py).**
   - **Extract all the perturbed structures in the 50 folders to the perturbation_structures folder (python extract.py).**
6. **Batch DFT Calculations**  
   Perturbed configurations are automatically processed through high-throughput density functional theory (DFT) calculations to obtain reference energies, forces, and stress tensors for MLIP training.
   - **Input files for high precision single point energy calculations can be found in the input_single_energy folder.**
   - **Highly accurate single-point energy calculations are performed on all perturbed structure batches (sh in_job.sh; sh jisuan.sh).**
   - **Check that high-precision single-point energy calculations for all perturbed structures converge normally (sh check.sh).**
7. **Build training set1**
   Extract atomic positions, energies, and forces from the batch DFT calculations to generate Training Set 1.(using the script single_energy2xyz.sh in vasp2xyz floder)
## Implementation Notes
- Ensure AIMD simulation length provides sufficient phase-space coverage
- Adjust perturbation magnitudes based on system properties
- Validate DFT convergence parameters before batch submissions
- Recommended workflow tools: ASE, VASP

This structured approach ensures generation of physically meaningful training data while maintaining computational feasibility for MLIP development.
