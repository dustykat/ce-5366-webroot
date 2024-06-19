#!/usr/bin/env python
# coding: utf-8

# # Modeling for Decision Support
# 
# Design and management decisions that are made about environmental and water resources systems, are based on what the decision-makers believe will take place as a result of their decisions. 
# These predictions are either based on very qualitative informa-
# tion or, at least in part, on quantitative information provided by an analog (mouse model for drug toxicity; column study for pollutant transport; ...), and/or mathematical (computer-based) models. 
# These quantitative mathematical models are considered essential for carrying out environmental impact assessments. 
# Mathematical simulation and optimization models packaged within interactive computer programs provide a common way
# for planners and managers to predict the behaviour of any proposed water resources system design or management policy before it is implemented
# 
# Modelling provides the principal way of predicting the behaviour of proposed infrastructural designs or management policies. The past thirty years have witnessed major advances in our abilities to model the engineering, economic, ecological, hydrological and sometimes even the institutional or political impacts of large, complex, multipurpose water resources systems. Appli-
# cations of models to real systems improves understanding, and contributes to improved system design, management and operation.
# 
# Problems motivating modelling and analyses exhibit a number of common characteristics:
# 
# >A systems focus or orientation. In such situations atten-
# tion needs to be devoted to the interdependencies and
# interactions of elements within the system as a whole,
# as well as to the elements themselves.
# 
# >The use of interdisciplinary teams. In many complex and non-traditional problems it is not at all clear from the start what disciplinary viewpoints will turn out to be most appropriate or acceptable. It is essential that participants in such work – coming from different established disciplines – become familiar with the
# techniques, vocabulary and concepts of the other
# disciplines involved. Participation in interdisciplinary
# modelling often requires a willingness to make mistakes at the fringes of one’s technical competence and
# to accept less than the latest advances in one’s own
# discipline.
# 
# >The use of formal mathematics. Most analysts prefer
# to use mathematical models to assist in system
# description and the identification and evaluation of
# efficient tradeoffs among conflicting objectives, and to
# provide an unambiguous record of the assumptions
# and data used in the analysis.
# 
# Not all water resources planning and management problems are suitable candidates for study using modelling
# methods. Modelling is most appropriate when:
# 
# >The planning and management objectives are reasonably well defined and organizations and individuals can be identified who can benefit from understanding the model results.
# 
# >There are many alternative decisions that may satisfy the stated objectives, and the best decision is not obvious.
# 
# >The water resources system and the objectives being analysed are describable by reasonably tractable mathematical representations.
# 
# >The information needed, such as the hydrological, economic, environmental and ecological impacts resulting from any decision, can be better estimated through the use of models.
# 
# > The parameters of these models are estimable from readily obtainable data.
# 
# ## Model Building Approach
# 
# The modeling approach distilled into a protocol (vaguely reminiscent of the scientific method) is summarized as:
# 
# 1. Identify the information the model is to provide. This includes criteria or measures of system performance that are of interest to stakeholders. These criteria or measures are defined as functions of the behaviour or state of the system being modelled. 
# 2. Model the behaviour so the state of the system associated with any ‘external’ inputs can be predicted. This requires modelling the physical, chemical, biological, economic, ecological and social processes that take place, as applicable, in the represented system. 
# 3. Integrate these two parts along with some means of entering the ‘external’ inputs and obtaining in meaningful ways the outputs.
# 4. Calibrate and verify or validate. 
# 5. Apply the model to produce the information desired.
# 
# There is a fair amount of effort in the steps above, and a lot of art. But even using software for a specific situation involves these steps in some sense.
# 
# ## Simulation Models
# 
# Simulation models address "what if" questions: What will likely happen over time and at one or more specific places if a particular design and/or operating policy is implemented?
# 
# Simulation works well when there are only a relatively few alternatives to be evaluated, not when there are a large number of them. The trial and error process of simulation is time consuming. An important role of optimization methods is to reduce the number of alternatives for simulation analyses. However, if only one method of analysis is to be used to evaluate a complex water resources system, simulation together with human judgement concerning which alternatives to simulate is often, and rightly so, the method of choice.

# ## Useful Model Types:
# 
# ### Hydrologic Models
# 
# - Rainfall-Runoff
# - Riverine/Flooding
# - other

# ### Water Quality Models
# 
# Water quality management has been mostly performed empirically, based mainly on political motivation and to a lesser extent on adequate scientific  information and analysis. 
# The need for more scientifically sound analyses has led to the creation of a large number of water 
# quality models; most of these models were developed for specific quality problems encountered in specific environmental and socioeconomic conditions.  
# 
# Water quality models can be classified according to the: 
# - Type of approach (physically based, conceptual, empirical) 
# - Pollutant item (nutrients, sediments, salts etc.) 
# - Area of application (catchment, groundwater, river system, coastal waters, integrated) 
# - Nature (Deterministic or Stochastic) 
# - State analysed (steady state or dynamic simulation) 
# - Spatial analysis (lumped, distributed) 
# -  Dimensions (1-D or 2-D models) 
# - Data requirements (extensive databases, minimum requirements models (MIR)) 
# 
# Water quality models are the key tools to test the impact of various actions on the quality of water bodies. Any attempt for effective water resources management in a river basin could be supported by water quality modelling. Each type of water body (estuary, river ...) needs the appropriate type of model. 
# 
# Some examples include:
# 
# The software code **DRAINMOD** is developed to assist in the simulation of the transport of 
# water and the transport and transformation of nitrogen in a stream (Skaggs 1981). DRAINMOD 
# model was first used as a research tool to investigate the performance of sub-irrigation and drainage 
# systems and their effects on pollutant treatment, crop response and water use (Skaggs et al.1981, 
# Massey et al.1983, Deal et al.1986). The most recent DRAINMOD PC version is the 6.1 released 
# on February 2012. DRAINMOD has been extended to predict the movement of nitrogen 
# (DRAINMOD-N) and salt (DRAINMOD-S) in shallow water table soils. 
# 
# The **Export Coefficient Model (ECM)** approach which was originally developed in 1976 (Omernik 1976) is not a data demanding model, it is simple and logical, while the limited data requirements make the approach 
# useful for catchment management and assessment (Johnes 1996, Burt and Johnes 1997, Johnes and 
# Butterfield 2002). 
# 
# The ECM has been widely used in several countries to predict the total amount of phosphorus 
# and nitrogen delivered to any given surface water sampling site (Bowes et al. 2008, European 
# Commission 2003a, European Commission 2003b, European Commission 2003c, Johnes 1996, 
# Ierodiaconou et al. 2005).  
# 
# The ECM approach aims to predict the nutrient loading at any surface water sampling site as a 
# function of the export of nutrients from each contamination source in the catchment above that site 
# (Johnes 1996). The ECM model relies on data from readily available databases. In order to avoid 
# the complications of predicting the concentration of individual phosphorous fractions and nitrogen 
# species introduced by nutrient cycling processes in surface water bodies, the ECM predictions can 
# be expressed as the mean annual concentrations of T-N and T-P in the surface water body by taking 
# account of the total annual discharge at the sampling site (Johnes 1996). Many researchers (Johnes 
# 1996, Heathwaite and Johnes 1996) reported that T-N and T-P are more reliable indicators of 
# changes in nutrient loading since they show markedly less seasonal variation than the 
# concentrations of NO3-, NO2-, NH4+, dissolved N, particulate organic N, PO43-, soluble P and 
# insoluble unreactive P. The model was initially adapted for UK conditions by Johnes and 
# O’Sullivan (1989); while it was further modified by Johnes (1996) in order to take into account the 
# following nutrient export factors: (a) areas of semi-natural woodland and vegetation; (b) cultivation 
# of specific crop types including winter and spring cereal crops, oilseed rape, field vegetables and 
# root vegetables, temporary, permanent and rough grassland; (c) human settlements and 
# sewage/septic tank systems. This version of the model runs at catchment scale using export 
# coefficients selected from the literature or within-catchment field experiments to produce a 
# calibrated model fit to observed nutrient load at the catchment outlet
# 
# **MIKE-11** is a one dimensional hydrodynamic model that simulates the dynamic water 
# movements in a river (DHI 1998). The model is well suited to complex systems and has been 
# applied as a water quality model to rivers in northern India and England (Crabtree et al. 1996, 
# Kazmi and Hansen 1997). It requires large amounts of data and remains a deterministic model. It 
# consists of a set of modules including: sediment transport, water quality, advection-dispersion, 
# rainfall-runoff and eutrophication. It can be used both as a water quality model to assess the impact 
# of intermittent discharges on rivers and as a hydraulic model by flood defense analysts and 
# designers.  
# 
# The **MONERIS** (MOdelling Nutrient Emissions in RIver Systems) model builds over eight sub-
# models that simulate the main processes of generation and transport of suspended solids and 
# nutrients to the river network (Behrendt et al. 2007, Palmeri et al. 2005). Since many countries are 
# moving forward a watershed-based approach as proposed by the WFD, the MONERIS model is 
# configured to support environmental studies in a watershed context (Venohr et al.2009). MONERIS 
# is a GIS-oriented model which is based on the empirical approach to describe complex relationships 
# in a simple way. It is a conceptual model for the quantification of nutrient emissions from point and 
# non-point sources in river catchments larger than 50 km2 (Behrendt et al. 2000). 
# The model includes a scenario manager in order to calculate the effects of measures on the 
# emissions of nutrients for different spatial units and pathways. The main processes and pathways in 
# MONERIS model are presented in Figure 1: (a) groundwater, (b) erosion, (c) overland flow 
# (dissolved nutrients), (d) tile drainages, (e) atmospheric deposition on water surface areas, (f) urban 
# areas, and (g) point sources (e.g. waste water treatment plants). 
# 
# **SIMCAT** (SIMulation of CATchments) is a one dimensional, deterministic, steady state (i.e. 
# time invariant) model that represents the fate and transport of solutes in the river and the inputs 
# from point-source effluent discharges on the basis of the following types of behaviour: (a) 
# Dissolved Oxygen is represented by a relationship involving temperature, reaeration and BOD 
# decay, (b) non-conservative substances which decay (i.e. nitrate and BOD), and (c) conservative 
# substances which are assumed not to decay. It is a stochastic model that makes use of Monte Carlo analysis techniques (with rich Corinthian leather!). The model was developed to assist in the process of planning the measures needed to improve water quality in the United Kingdom (Warn 2010). 
# 
# The **TOMCAT** model (Temporal/Overall Model for CATchments) makes use of Monte Carlo 
# analysis and was developed to assist in the process of reviewing effluent quality standards at 
# sampling sites, in order to meet the objectives of surface water quality preservation (Bowden and 
# Brown 1984). 
# The model allows for more complex temporal correlations taking into account the seasonal and 
# diurnal effects in the flow data and the recorded water quality and then reproduces these effects in 
# the simulated data. A number of contamination events that are specified at the rivers, monitoring 
# sites, abstractions and effluent discharges define the river system in TOMCAT. 
# 
# **TOPCAT** model uses subsurface flow equations and identical soil moisture stores, while it is a 
# minimum information requirement (MIR) version of TOPMODEL (Quinn and Beven 1993). A 
# nitrate model (N-MIR) and phosphorous model (P-MIR) constitute TOPCAT-NP model which is 
# able to predict hourly or daily nitrate and phosphorous losses (Quinn et al.1999). This model is 
# applicable at a research scale within instrumented sites (1-10 km2) and more generally at the wider 
# catchment scale (100-1500 km2). 
# 
# **QUAL2K** is a one dimensional, steady-state model of water quality and in-stream flow. It is 
# neither stochastic nor dynamic simulation model. The QUAL2K model can simulate up to 16 water 
# quality determinants along a river and its tributaries (Brown and Barnwell 1987). The river reach is 
# divided into a number of subreaches of equal length. The model uses the following assumptions: (a) 
# the advective transport is based on the mean flow, (b) the water quality indicators completely are 
# completely mixed over the cross-section and (c) the dispersive transport is correlated with the 
# concentration gradient.  
# 
# The model allows the user to simulate any combination of the following determinants: (a) 
# Dissolved Oxygen, (b) Temperature, (c) Phosphorous, (d) Nitrate, Nitrite, Ammonium and Organic 
# Nitrogen, (e) Chlorophyll-a, (f) up to three conservative solutes, (g) one non-conservative 
# constituent solute, and (h) coliform bacteria. 
# 
# Furthermore, Nitrate, Phosphate and Dissolved Oxygen are represented in more detail; while 
# most determinants are simulated as first order decay. The QUAL2K model is suitable for modelling 
# pollutants in freshwater that rely on sediment interactions, especially as a sink of inorganic and 
# organic substances. The initial step of the standard QUAL2K model is to divide the river system 
# into reaches (up to 50) and each of these is then divided into computational elements (up to 20 per 
# reach) of equal length. 
# 
# The data requirements of the model in terms of flow and water quality data include single values 
# of each determinant being modeled. The main feature of this model is the river reach. The data 
# required for each river reach include: (a) flow data and hydraulic terms, (b) initial conditions, (c) 
# reaction rate coefficients, (d) local climatological data for heat balance computations, and (e) rate 
# parameters for all of the biological and chemical reactions. 
# 
# The output of the model includes solutions to the pollutant mass balance and the flow for each 
# reach. The main advantage of QUAL2K is the capability of simulation of algae (Chlorophyll-a), an 
# extensive documentation of its code and theoretical background. QUALK2K is available for free 
# download from its website. The model requires a small amount of data to represent the sediments 
# and only partial hydraulic terms.

# ## Hydraulic Models
# 
# - Riverine Hydraulics
# - Overland SWMM
# - Distribution System EPANET

#  

# ### Cost Models
# 
# Modelling, (Darby ,2000), is the reduction of a real-world phenomenon of interest into a construct or set of constructs called symbolic models, which captures specific system behaviours. When applied to building project cost models, the model emulates the cost structure system, budget allocation, cost consumption and cost performance review within a project. Projects are often governed by constraints such as resources (budget, manpower, material and overheads), the project schedule, and the customer's project requirements etc. As an end effort, the cost model is often expressed on paper and worked out using calculator, before converting it into a software application.
# 
# Cost models, like all models, have their own limitations. Models allow the model builder to emphasise or ignore certain aspects of the reality, depending upon the purpose of the model. Models inevitably overlook, rearrange or distort some details of the reality. A lack of correspondence between the reality and the model may lead to decisions being made on the basis of incorrect information (Beaman, Ranatunga, Krueger & Mudalige, 1998, p.3). Thus, the need for a good correlation between reality and model is a key goal of this research, which seeks to establish a set of success dimensions or criteria for the development of effective cost models for project cost management. A ‘dimensionally enhanced’ approach to cost modelling focuses on the ontological aspect, in defining the essential ‘what’ rather than the ‘how’ of the model. According to Banathy (1996), the ontological task is the formation of a systems view of what is in the broadest sense a systems view of the world. This can lead to a new orientation for scientific inquiry.
# 
# **A Systemic Approach To Cost Modelling**
# 
# Banathy (1996, p.74) asserts that a systems view enables exploration and characterization of the system of our interest, its environment, and its components and parts. We can acquire a systems view by *integrating* systems concepts and principles into our thinking and learning and the way we represent our experiences and our world. When adapted to a costing system, the systems view represents an inquiry process that will generate the following insights:
# 
# - Characteristics of the “embeddedness” of costing systems operating at several interconnected levels (e.g. project management, cost modelling, end-user operation, senior manager reporting, system administration, organisation learning, financial and business process improvement levels).
# - Relationships, interactions, and mutual interdependencies of systems operating at those levels.
# - The purposes, goals, and boundaries of costing systems.
# - Relationships, interactions, and information/data/instructions exchanges between systems and their environment.
# - Dynamics of the interactions, relationships, and patterns of connectedness amongst the components of the costing systems.
# - Properties of wholeness and the characteristics that emerge at various systems levels as a result of systemic interaction and synthesis.
# - System processes, and the behaviour and change of system and their environment over time.
# 
# <!--The Inquiry Process for Cost Modelling
# 
# According to McDermott (1981), inquiry is the controlled or directed transformation of an indeterminate situation into one that is so determinate in its constituent distinctions and relations, as to convert the elements of the original situation into a unified whole. During the inquiry process, a set of ‘guiding questions’ is needed to help the project managers to capture the essential information needed to build the cost model. In this research, the set of ‘guiding questions’ is embodied in the list of nine success criteria identified as being necessary to achieve effective cost modelling. The nine success criteria were first derived from a 9-step process for building the life cycle costing (LCC) model for vehicle fleet management that I had adopted in my course of work. The 9-step LCC process was evolved from the combination of my practical experience as a project manager and personal learning from the literature
# 
# In order to translate the nine steps into a set of ontological codes, I had used the sequence of six grounded theory actions proposed by Professor Bob Dick (2002) to condense my data and derive the success criteria for project cost modelling. The following actions were carried out for each of the LCC steps: data collection, note-taking, coding, memoing, sorting and writing. The following exhibit shows the coding and sorting of the entire set of nine LCC modelling steps and the associated themes. The third column shows the final codes that would represent the success criteria for project cost modelling.
# 
# ![](p3_01.png)
# 
# These codes can be grouped into three perspectives of cost modelling, namely structural, investment and results as shown in the final column. The criteria are grouped as follows:
# 
#    - Criterion 1 to 3 - Structural perspective of the PCM
#    - Criterion 4 to 6 - Investment perspective of the PCM
#    - Criterion 7 to 9 - Results perspective of the PCM -->
# 
# ### Integrated Models
# 
# Hydrologic and Drainage like SWMM.
# 
# Cost and Hydraulic like EPANET.

# 

# ## References
# 
# 1. [WRSPM pp. 39-55](http://54.243.252.9/ce-5333-systems-webroot/3-Readings/WaterResourcesSystemsPlanningManagement/WaterResourcesText.pdf) 
# 2. [Loucks, Stedenger, Haith (1981) Water Resources Systems Planning and Analysis p. 8](http://54.243.252.9/ce-5333-systems-webroot/3-Readings/SystemsCharacteristics/SystemsCharacteristics1.pdf) 
# 3. [Loucks, Stedenger, Haith (1981) Water Resources Systems Planning and Analysis p. 9](http://54.243.252.9/ce-5333-systems-webroot/3-Readings/SystemsCharacteristics/SystemsCharacteristics2.pdf)
# 4. [Goh, E. (2005). A systematic approach to effective project cost management. Paper presented at PMI® Global Congress 2005—Asia Pacific, Singapore. Newtown Square, PA: Project Management Institute.](https://www.pmi.org/learning/library/systematic-approach-effective-project-cost-management-7598)

# In[ ]:




