import cobra

sml_path = 'e_coli_core.xml'
sml = cobra.io.read_sbml_model(sml_path)

# Set the objective to biomass
sml.objective = sml.reactions.BIOMASS_Ecoli_core_w_GAM

# Optimize the model
result = sml.optimize()

# Print the objective value
print(result.objective_value)
print(result.status)
print(sml.summary())
