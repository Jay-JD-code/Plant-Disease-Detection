# Comprehensive Plant Disease Information Database

DISEASE_INFO = {
    'Apple___Apple_scab': {
        'name': 'Apple Scab',
        'plant': 'Apple',
        'severity': 'Moderate to Severe',
        'description': 'Apple scab is a fungal disease that affects apple trees, causing dark, scabby lesions on leaves, fruit, and twigs. It thrives in cool, wet conditions.',
        'symptoms': [
            'Dark, olive-green to brown spots on leaves',
            'Scabby lesions on fruit surface',
            'Premature leaf drop',
            'Reduced fruit quality and storage life',
            'Cracking and distortion of fruit'
        ],
        'causes': [
            'Fungal pathogen Venturia inaequalis',
            'Cool, wet spring weather',
            'High humidity (above 80%)',
            'Poor air circulation',
            'Infected plant debris'
        ],
        'organic_treatments': [
            'Apply sulfur-based fungicides during early growing season',
            'Use copper-based sprays (Bordeaux mixture)',
            'Apply neem oil as preventative measure',
            'Remove and destroy infected leaves and fruit',
            'Improve air circulation by pruning'
        ],
        'supplements': [
            {
                'name': 'Organic Sulfur Fungicide',
                'usage': 'Apply every 7-14 days during wet periods',
                'benefits': 'Prevents spore germination and infection'
            },
            {
                'name': 'Copper Sulfate',
                'usage': 'Spray during dormant season and early spring',
                'benefits': 'Provides protective barrier against fungal spores'
            },
            {
                'name': 'Potassium Bicarbonate',
                'usage': '1 tbsp per gallon of water, spray weekly',
                'benefits': 'Changes leaf surface pH to prevent fungal growth'
            },
            {
                'name': 'Compost Tea',
                'usage': 'Apply bi-weekly as soil drench and foliar spray',
                'benefits': 'Boosts plant immunity and beneficial microorganisms'
            }
        ],
        'prevention': [
            'Choose scab-resistant apple varieties',
            'Ensure proper spacing for air circulation',
            'Remove fallen leaves and fruit debris',
            'Apply dormant oil sprays',
            'Avoid overhead watering'
        ]
    },
    
    'Apple___Black_rot': {
        'name': 'Apple Black Rot',
        'plant': 'Apple',
        'severity': 'Severe',
        'description': 'Black rot is a serious fungal disease that affects apple trees, causing fruit rot and cankers on branches. It can lead to significant crop losses.',
        'symptoms': [
            'Brown to black circular lesions on fruit',
            'Mummified fruit that remains on tree',
            'Cankers on branches and trunk',
            'Leaf spots with concentric rings',
            'Premature fruit drop'
        ],
        'causes': [
            'Fungal pathogen Botryosphaeria obtusa',
            'Stress from drought or injury',
            'Poor sanitation practices',
            'Wounds in bark or fruit',
            'High temperature and humidity'
        ],
        'organic_treatments': [
            'Remove and destroy infected fruit and wood',
            'Apply copper-based fungicides',
            'Prune out cankers during dormant season',
            'Use lime sulfur spray',
            'Improve tree health and vigor'
        ],
        'supplements': [
            {
                'name': 'Copper Fungicide',
                'usage': 'Apply during dormant season and pre-bloom',
                'benefits': 'Prevents new infections and kills existing spores'
            },
            {
                'name': 'Lime Sulfur',
                'usage': 'Spray during dormant period',
                'benefits': 'Eradicates overwintering spores and eggs'
            },
            {
                'name': 'Bacillus subtilis',
                'usage': 'Apply as directed during growing season',
                'benefits': 'Biological control agent that inhibits fungal growth'
            },
            {
                'name': 'Fish Emulsion Fertilizer',
                'usage': 'Apply monthly during growing season',
                'benefits': 'Strengthens plant immunity and overall health'
            }
        ],
        'prevention': [
            'Maintain good sanitation practices',
            'Prune for proper air circulation',
            'Avoid mechanical injuries',
            'Water at soil level, not on foliage',
            'Apply balanced fertilizer regularly'
        ]
    },
    
    'Apple___Cedar_apple_rust': {
        'name': 'Cedar Apple Rust',
        'plant': 'Apple',
        'severity': 'Moderate',
        'description': 'A fungal disease that requires both apple and cedar trees to complete its life cycle. It causes distinctive orange spots on apple leaves.',
        'symptoms': [
            'Bright orange spots on upper leaf surface',
            'Small tube-like projections on leaf undersides',
            'Premature defoliation',
            'Reduced fruit quality',
            'Orange gelatinous masses on cedar trees'
        ],
        'causes': [
            'Fungal pathogen Gymnosporangium juniperi-virginianae',
            'Presence of cedar/juniper trees nearby',
            'Cool, wet spring conditions',
            'High humidity levels',
            'Wind dispersal of spores'
        ],
        'organic_treatments': [
            'Remove cedar trees within 1 mile if possible',
            'Apply sulfur-based fungicides',
            'Use resistant apple varieties',
            'Spray with copper fungicide',
            'Improve air circulation around trees'
        ],
        'supplements': [
            {
                'name': 'Wettable Sulfur',
                'usage': 'Apply every 7-10 days during wet periods',
                'benefits': 'Prevents spore germination and disease development'
            },
            {
                'name': 'Propiconazole',
                'usage': 'Apply at pink stage and petal fall',
                'benefits': 'Systemic fungicide for cedar apple rust control'
            },
            {
                'name': 'Myclobutanil',
                'usage': 'Spray at 2-week intervals during infection period',
                'benefits': 'Effective against rust diseases'
            },
            {
                'name': 'Kelp Meal',
                'usage': 'Work into soil around tree base in spring',
                'benefits': 'Provides trace elements and boosts plant resistance'
            }
        ],
        'prevention': [
            'Plant rust-resistant apple varieties',
            'Remove nearby cedar and juniper trees',
            'Ensure good air circulation',
            'Avoid overhead irrigation',
            'Apply preventive fungicide sprays'
        ]
    },

    'Tomato_Bacterial_spot': {
        'name': 'Bacterial Spot',
        'plant': 'Tomato',
        'severity': 'Moderate to Severe',
        'description': 'A bacterial disease that affects tomatoes, causing leaf spots, defoliation, and fruit lesions. It spreads rapidly in warm, humid conditions.',
        'symptoms': [
            'Small, dark spots on leaves with yellow halos',
            'Defoliation starting from lower leaves',
            'Raised, scab-like spots on fruit',
            'Reduced fruit quality and yield',
            'Stem cankers in severe cases'
        ],
        'causes': [
            'Bacterial pathogen Xanthomonas species',
            'Warm, humid weather conditions',
            'Overhead watering or rain splash',
            'Contaminated seeds or transplants',
            'Poor air circulation'
        ],
        'organic_treatments': [
            'Apply copper-based bactericides',
            'Remove infected plant debris',
            'Improve air circulation',
            'Use drip irrigation instead of overhead',
            'Rotate crops annually'
        ],
        'supplements': [
            {
                'name': 'Copper Hydroxide',
                'usage': 'Spray every 7-14 days during favorable conditions',
                'benefits': 'Bactericidal action against Xanthomonas'
            },
            {
                'name': 'Streptomycin',
                'usage': 'Apply during early disease development',
                'benefits': 'Antibiotic effective against bacterial pathogens'
            },
            {
                'name': 'Bacillus amyloliquefaciens',
                'usage': 'Apply as preventive biological control',
                'benefits': 'Beneficial bacteria that suppresses pathogens'
            },
            {
                'name': 'Calcium Chloride',
                'usage': 'Foliar spray at 0.5% solution',
                'benefits': 'Strengthens cell walls and reduces infection'
            }
        ],
        'prevention': [
            'Use certified disease-free seeds',
            'Practice crop rotation',
            'Provide adequate plant spacing',
            'Avoid working with wet plants',
            'Disinfect tools regularly'
        ]
    },

    'Tomato_Early_blight': {
        'name': 'Early Blight',
        'plant': 'Tomato',
        'severity': 'Moderate',
        'description': 'A common fungal disease that affects tomato plants, causing characteristic target-like spots on leaves and stems.',
        'symptoms': [
            'Brown spots with concentric rings (target spots)',
            'Lower leaves affected first',
            'Yellowing and dropping of leaves',
            'Stem cankers near soil line',
            'Fruit lesions with dark, leathery appearance'
        ],
        'causes': [
            'Fungal pathogen Alternaria solani',
            'High humidity and warm temperatures',
            'Poor air circulation',
            'Water stress',
            'Nutrient deficiencies'
        ],
        'organic_treatments': [
            'Apply baking soda spray (1 tsp per quart water)',
            'Use copper-based fungicides',
            'Remove infected plant material',
            'Mulch around plants',
            'Improve air circulation'
        ],
        'supplements': [
            {
                'name': 'Chlorothalonil',
                'usage': 'Apply every 7-14 days preventively',
                'benefits': 'Broad-spectrum fungicide for early blight control'
            },
            {
                'name': 'Azoxystrobin',
                'usage': 'Rotate with other fungicides',
                'benefits': 'Systemic fungicide with long-lasting protection'
            },
            {
                'name': 'Compost',
                'usage': 'Apply 2-3 inches around plants',
                'benefits': 'Improves soil health and plant resistance'
            },
            {
                'name': 'Epsom Salt',
                'usage': '1 tbsp per gallon, spray monthly',
                'benefits': 'Provides magnesium for stronger plant structure'
            }
        ],
        'prevention': [
            'Choose resistant varieties when available',
            'Space plants properly for air circulation',
            'Water at soil level, not on leaves',
            'Mulch to prevent soil splash',
            'Remove lower leaves that touch ground'
        ]
    },

    'Corn_(maize)___Common_rust_': {
        'name': 'Common Rust',
        'plant': 'Corn/Maize',
        'severity': 'Moderate',
        'description': 'A fungal disease that creates rust-colored pustules on corn leaves, affecting photosynthesis and yield.',
        'symptoms': [
            'Small, reddish-brown pustules on leaves',
            'Pustules rupture to release rust spores',
            'Yellowing and premature death of leaves',
            'Reduced photosynthetic area',
            'Weakened stalks susceptible to lodging'
        ],
        'causes': [
            'Fungal pathogen Puccinia sorghi',
            'Cool, humid weather conditions',
            'Dense plant populations',
            'Presence of alternate host (wood sorrel)',
            'Wind dispersal of spores'
        ],
        'organic_treatments': [
            'Plant resistant corn varieties',
            'Apply sulfur-based fungicides',
            'Remove alternate hosts nearby',
            'Ensure proper plant spacing',
            'Use foliar fungicides if needed'
        ],
        'supplements': [
            {
                'name': 'Propiconazole',
                'usage': 'Apply at first sign of disease',
                'benefits': 'Systemic fungicide effective against rust'
            },
            {
                'name': 'Azoxystrobin + Propiconazole',
                'usage': 'Tank mix for broader spectrum control',
                'benefits': 'Combines contact and systemic action'
            },
            {
                'name': 'Potassium Phosphite',
                'usage': 'Foliar spray every 2 weeks',
                'benefits': 'Enhances plant defense mechanisms'
            },
            {
                'name': 'Zinc Sulfate',
                'usage': 'Apply as foliar spray at V6-V8 stage',
                'benefits': 'Micronutrient that boosts plant immunity'
            }
        ],
        'prevention': [
            'Select rust-resistant hybrids',
            'Plant at recommended population densities',
            'Monitor weather conditions',
            'Scout fields regularly',
            'Control alternate hosts'
        ]
    },

    'Potato___Early_blight': {
        'name': 'Early Blight',
        'plant': 'Potato',
        'severity': 'Moderate to Severe',
        'description': 'A fungal disease that affects potato foliage and tubers, characterized by dark brown lesions with concentric rings.',
        'symptoms': [
            'Dark brown lesions with target-like rings',
            'Yellowing of leaves around lesions',
            'Defoliation starting from lower leaves',
            'Dark, sunken lesions on tubers',
            'Reduced tuber quality and storage life'
        ],
        'causes': [
            'Fungal pathogen Alternaria solani',
            'High temperature and humidity',
            'Plant stress from drought or nutrient deficiency',
            'Dense foliage with poor air circulation',
            'Infected seed tubers'
        ],
        'organic_treatments': [
            'Apply copper-based fungicides',
            'Use preventive fungicide sprays',
            'Remove and destroy infected foliage',
            'Improve soil drainage',
            'Practice crop rotation'
        ],
        'supplements': [
            {
                'name': 'Mancozeb',
                'usage': 'Apply every 7-10 days during favorable conditions',
                'benefits': 'Protectant fungicide for early blight control'
            },
            {
                'name': 'Chlorothalonil',
                'usage': 'Alternate with mancozeb for resistance management',
                'benefits': 'Broad-spectrum contact fungicide'
            },
            {
                'name': 'Calcium Nitrate',
                'usage': 'Apply as side-dress during tuber development',
                'benefits': 'Provides calcium for stronger cell walls'
            },
            {
                'name': 'Seaweed Extract',
                'usage': 'Foliar spray every 2-3 weeks',
                'benefits': 'Contains growth hormones and trace elements'
            }
        ],
        'prevention': [
            'Use certified disease-free seed potatoes',
            'Practice 3-4 year crop rotation',
            'Maintain adequate soil fertility',
            'Avoid overhead irrigation',
            'Hill soil properly around plants'
        ]
    },

    # Add healthy conditions
    'Apple___healthy': {
        'name': 'Healthy Apple',
        'plant': 'Apple',
        'severity': 'Healthy',
        'description': 'This apple plant appears healthy with no visible signs of disease. Continue proper care and monitoring.',
        'symptoms': [
            'Green, vibrant foliage',
            'No visible spots or lesions',
            'Normal growth pattern',
            'Good leaf color and texture',
            'No signs of stress'
        ],
        'causes': [
            'Proper plant care and maintenance',
            'Adequate nutrition and watering',
            'Good air circulation',
            'Disease prevention practices',
            'Healthy growing conditions'
        ],
        'organic_treatments': [
            'Continue current care routine',
            'Monitor regularly for any changes',
            'Maintain proper watering schedule',
            'Apply preventive measures during disease season',
            'Keep area clean of debris'
        ],
        'supplements': [
            {
                'name': 'Balanced Organic Fertilizer',
                'usage': 'Apply according to package directions',
                'benefits': 'Maintains overall plant health and vigor'
            },
            {
                'name': 'Compost',
                'usage': 'Apply 2-3 inch layer around base',
                'benefits': 'Improves soil structure and provides nutrients'
            },
            {
                'name': 'Kelp Meal',
                'usage': 'Mix into soil in early spring',
                'benefits': 'Provides trace minerals and growth hormones'
            },
            {
                'name': 'Mycorrhizal Inoculant',
                'usage': 'Apply at planting or work into existing soil',
                'benefits': 'Enhances nutrient uptake and root health'
            }
        ],
        'prevention': [
            'Continue regular monitoring',
            'Maintain proper sanitation',
            'Ensure adequate nutrition',
            'Provide appropriate watering',
            'Practice preventive treatments as needed'
        ]
    },

    'Tomato_healthy': {
        'name': 'Healthy Tomato',
        'plant': 'Tomato',
        'severity': 'Healthy',
        'description': 'This tomato plant shows excellent health with vibrant foliage and no disease symptoms.',
        'symptoms': [
            'Deep green, healthy leaves',
            'Strong stem structure',
            'Normal flowering and fruit set',
            'No discoloration or spots',
            'Vigorous growth'
        ],
        'causes': [
            'Optimal growing conditions',
            'Proper nutrition and care',
            'Good disease management',
            'Adequate water and sunlight',
            'Healthy soil conditions'
        ],
        'organic_treatments': [
            'Maintain current care practices',
            'Continue regular watering and feeding',
            'Monitor for early signs of problems',
            'Practice preventive care',
            'Ensure good air circulation'
        ],
        'supplements': [
            {
                'name': 'Tomato Fertilizer (10-10-10)',
                'usage': 'Apply every 2-3 weeks during growing season',
                'benefits': 'Balanced nutrition for optimal growth'
            },
            {
                'name': 'Calcium Supplement',
                'usage': 'Apply to prevent blossom end rot',
                'benefits': 'Strengthens cell walls and fruit development'
            },
            {
                'name': 'Organic Matter',
                'usage': 'Work into soil before planting',
                'benefits': 'Improves soil structure and water retention'
            },
            {
                'name': 'Beneficial Bacteria',
                'usage': 'Apply as soil drench monthly',
                'benefits': 'Enhances root health and nutrient uptake'
            }
        ],
        'prevention': [
            'Continue excellent care practices',
            'Monitor environmental conditions',
            'Maintain proper plant spacing',
            'Practice crop rotation',
            'Keep tools and area clean'
        ]
    },

    # Corn diseases
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': {
        'name': 'Gray Leaf Spot',
        'plant': 'Corn (Maize)',
        'severity': 'Moderate to Severe',
        'description': 'A fungal disease that causes rectangular gray lesions on corn leaves, reducing photosynthetic capacity and yield.',
        'symptoms': [
            'Rectangular gray to tan lesions on leaves',
            'Lesions have distinct margins parallel to leaf veins',
            'Yellowing and premature death of leaves',
            'Reduced ear size and grain fill',
            'Increased stalk lodging susceptibility'
        ],
        'causes': [
            'Fungal pathogen Cercospora zeae-maydis',
            'High humidity and warm temperatures (75-85°F)',
            'Extended periods of leaf wetness',
            'Dense plant populations',
            'Corn residue from previous seasons'
        ],
        'organic_treatments': [
            'Apply copper-based fungicides',
            'Use resistant corn hybrids',
            'Improve air circulation with proper spacing',
            'Remove and destroy infected plant debris',
            'Rotate crops to non-grass species'
        ],
        'supplements': [
            {
                'name': 'Azoxystrobin',
                'usage': 'Apply at VT to R1 growth stage',
                'benefits': 'Systemic fungicide providing long-lasting control'
            },
            {
                'name': 'Propiconazole',
                'usage': 'Apply preventively before disease onset',
                'benefits': 'Effective triazole fungicide for gray leaf spot'
            },
            {
                'name': 'Potassium Fertilizer',
                'usage': 'Apply adequate K at planting and sidedress',
                'benefits': 'Strengthens plant cell walls and disease resistance'
            },
            {
                'name': 'Manganese Sulfate',
                'usage': 'Foliar application during vegetative growth',
                'benefits': 'Micronutrient that enhances disease tolerance'
            }
        ],
        'prevention': [
            'Choose resistant or tolerant hybrids',
            'Practice crop rotation with soybeans or other non-hosts',
            'Manage corn residue through tillage',
            'Avoid excessive nitrogen fertilization',
            'Monitor fields regularly during humid periods'
        ]
    },

    'Corn_(maize)___Northern_Leaf_Blight': {
        'name': 'Northern Leaf Blight',
        'plant': 'Corn (Maize)',
        'severity': 'Moderate to Severe',
        'description': 'A fungal disease causing large, cigar-shaped lesions on corn leaves, significantly impacting photosynthesis and yield.',
        'symptoms': [
            'Large, elliptical gray-green lesions on leaves',
            'Lesions are 1-6 inches long with distinct borders',
            'Dark green to gray coloration of lesions',
            'Lesions may have concentric zones',
            'Premature leaf death and stalk lodging'
        ],
        'causes': [
            'Fungal pathogen Exserohilum turcicum',
            'Cool, humid weather conditions',
            'Temperature range 65-80°F with high moisture',
            'Corn debris from previous seasons',
            'Dense plant canopies with poor air circulation'
        ],
        'organic_treatments': [
            'Apply foliar fungicides at early disease onset',
            'Use genetically resistant corn varieties',
            'Improve field drainage and air circulation',
            'Remove infected crop residue',
            'Practice crop rotation'
        ],
        'supplements': [
            {
                'name': 'Strobilurin Fungicides',
                'usage': 'Apply at V8 to VT growth stages',
                'benefits': 'Preventive control with systemic activity'
            },
            {
                'name': 'Triazole Fungicides',
                'usage': 'Apply when disease first appears',
                'benefits': 'Curative and protective action against fungus'
            },
            {
                'name': 'Balanced NPK Fertilizer',
                'usage': 'Apply according to soil test recommendations',
                'benefits': 'Maintains plant health and stress tolerance'
            },
            {
                'name': 'Silicate Amendments',
                'usage': 'Apply to soil before planting',
                'benefits': 'Strengthens plant cell walls against pathogens'
            }
        ],
        'prevention': [
            'Plant resistant or tolerant corn hybrids',
            'Practice minimum 2-year crop rotation',
            'Manage crop residue through tillage',
            'Avoid overhead irrigation during humid periods',
            'Monitor weather conditions for disease forecasting'
        ]
    },

    'Corn_(maize)___healthy': {
        'name': 'Healthy Corn',
        'plant': 'Corn (Maize)',
        'severity': 'Healthy',
        'description': 'This corn plant displays excellent health with vigorous growth and no visible disease symptoms.',
        'symptoms': [
            'Dark green, uniform leaf coloration',
            'Strong, upright growth habit',
            'Normal tassel and silk development',
            'No leaf lesions or discoloration',
            'Healthy root system development'
        ],
        'causes': [
            'Optimal growing conditions',
            'Proper soil fertility and pH',
            'Adequate moisture management',
            'Good pest and disease management',
            'Appropriate hybrid selection'
        ],
        'organic_treatments': [
            'Continue current management practices',
            'Monitor regularly for any changes',
            'Maintain consistent watering',
            'Practice preventive disease management',
            'Ensure proper nutrition'
        ],
        'supplements': [
            {
                'name': 'Starter Fertilizer (10-34-0)',
                'usage': 'Apply at planting for early growth',
                'benefits': 'Promotes rapid establishment and root development'
            },
            {
                'name': 'Side-dress Nitrogen',
                'usage': 'Apply at V6-V8 growth stage',
                'benefits': 'Supports vegetative growth and yield potential'
            },
            {
                'name': 'Micronutrient Blend',
                'usage': 'Apply based on soil test results',
                'benefits': 'Prevents deficiencies and optimizes plant health'
            },
            {
                'name': 'Organic Matter',
                'usage': 'Incorporate into soil before planting',
                'benefits': 'Improves soil structure and water holding capacity'
            }
        ],
        'prevention': [
            'Continue excellent management practices',
            'Regular scouting for pests and diseases',
            'Maintain proper plant population',
            'Practice appropriate crop rotation',
            'Monitor soil fertility levels'
        ]
    },

    # Pepper diseases
    'Pepper__bell___Bacterial_spot': {
        'name': 'Bacterial Spot',
        'plant': 'Pepper (Bell)',
        'severity': 'Moderate to Severe',
        'description': 'A bacterial disease affecting pepper plants, causing leaf spots, defoliation, and fruit lesions that reduce marketability.',
        'symptoms': [
            'Small, dark brown spots on leaves',
            'Spots have yellow halos initially',
            'Raised, scab-like lesions on fruit',
            'Defoliation during severe infections',
            'Reduced fruit quality and yield'
        ],
        'causes': [
            'Bacterial pathogen Xanthomonas species',
            'Warm, humid weather conditions',
            'Overhead irrigation or rain splash',
            'Contaminated seeds or transplants',
            'Wounds from insects or handling'
        ],
        'organic_treatments': [
            'Apply copper-based bactericides',
            'Remove and destroy infected plant material',
            'Improve air circulation around plants',
            'Use drip irrigation instead of overhead watering',
            'Practice crop rotation with non-solanaceous crops'
        ],
        'supplements': [
            {
                'name': 'Copper Hydroxide',
                'usage': 'Spray every 7-10 days during humid conditions',
                'benefits': 'Bactericidal action against Xanthomonas'
            },
            {
                'name': 'Streptomycin Sulfate',
                'usage': 'Apply during early infection stages',
                'benefits': 'Antibiotic effective against bacterial pathogens'
            },
            {
                'name': 'Bacillus subtilis',
                'usage': 'Apply as biological control agent',
                'benefits': 'Beneficial bacteria that inhibits pathogens'
            },
            {
                'name': 'Calcium Chloride',
                'usage': 'Foliar spray at 0.5% concentration',
                'benefits': 'Strengthens cell walls against bacterial invasion'
            }
        ],
        'prevention': [
            'Use certified disease-free seeds and transplants',
            'Practice 2-3 year crop rotation',
            'Provide adequate plant spacing',
            'Avoid working with plants when wet',
            'Disinfect tools and equipment regularly'
        ]
    },

    'Pepper__bell___healthy': {
        'name': 'Healthy Pepper',
        'plant': 'Pepper (Bell)',
        'severity': 'Healthy',
        'description': 'This bell pepper plant shows optimal health with vigorous growth and no disease symptoms.',
        'symptoms': [
            'Dark green, glossy leaves',
            'Strong branching structure',
            'Normal flower and fruit development',
            'No leaf spots or discoloration',
            'Vigorous root system'
        ],
        'causes': [
            'Optimal growing environment',
            'Proper soil nutrition and pH',
            'Adequate water management',
            'Good air circulation',
            'Effective pest and disease prevention'
        ],
        'organic_treatments': [
            'Maintain current care routine',
            'Continue regular monitoring',
            'Practice preventive measures',
            'Ensure consistent watering',
            'Provide adequate nutrition'
        ],
        'supplements': [
            {
                'name': 'Balanced Fertilizer (5-10-10)',
                'usage': 'Apply every 3-4 weeks during growing season',
                'benefits': 'Promotes healthy growth and fruit development'
            },
            {
                'name': 'Calcium Supplement',
                'usage': 'Apply during fruit development',
                'benefits': 'Prevents blossom end rot and strengthens plants'
            },
            {
                'name': 'Compost Tea',
                'usage': 'Apply bi-weekly as soil drench',
                'benefits': 'Provides nutrients and beneficial microorganisms'
            },
            {
                'name': 'Epsom Salt',
                'usage': '1 tablespoon per gallon water monthly',
                'benefits': 'Provides magnesium for chlorophyll production'
            }
        ],
        'prevention': [
            'Continue excellent care practices',
            'Regular inspection for problems',
            'Maintain proper plant spacing',
            'Practice good garden sanitation',
            'Monitor environmental conditions'
        ]
    },

    # Potato diseases
    'Potato___Late_blight': {
        'name': 'Late Blight',
        'plant': 'Potato',
        'severity': 'Severe',
        'description': 'A devastating fungal-like disease that can destroy entire potato crops rapidly under favorable conditions.',
        'symptoms': [
            'Water-soaked spots on leaves that turn brown',
            'White fuzzy growth on undersides of leaves',
            'Dark brown lesions on stems',
            'Firm, brown rot on tubers',
            'Rapid plant collapse in humid conditions'
        ],
        'causes': [
            'Oomycete pathogen Phytophthora infestans',
            'Cool, wet weather conditions (60-70°F)',
            'High humidity and extended leaf wetness',
            'Poor air circulation',
            'Infected seed tubers or volunteer plants'
        ],
        'organic_treatments': [
            'Apply copper-based fungicides preventively',
            'Remove and destroy infected plants immediately',
            'Improve drainage and air circulation',
            'Use resistant potato varieties when available',
            'Practice strict sanitation measures'
        ],
        'supplements': [
            {
                'name': 'Copper Sulfate',
                'usage': 'Apply before disease onset and regularly',
                'benefits': 'Protective fungicide against late blight'
            },
            {
                'name': 'Metalaxyl + Mancozeb',
                'usage': 'Apply according to disease forecast',
                'benefits': 'Systemic and contact fungicide combination'
            },
            {
                'name': 'Potassium Phosphite',
                'usage': 'Foliar spray every 7-14 days preventively',
                'benefits': 'Enhances plant defense mechanisms'
            },
            {
                'name': 'Seaweed Extract',
                'usage': 'Regular foliar applications',
                'benefits': 'Strengthens plant immunity and stress tolerance'
            }
        ],
        'prevention': [
            'Use certified disease-free seed potatoes',
            'Plant resistant or tolerant varieties',
            'Ensure good field drainage',
            'Monitor weather conditions closely',
            'Remove volunteer potato plants'
        ]
    },

    'Potato___healthy': {
        'name': 'Healthy Potato',
        'plant': 'Potato',
        'severity': 'Healthy',
        'description': 'This potato plant exhibits excellent health with robust foliage and proper development.',
        'symptoms': [
            'Bright green, healthy foliage',
            'Strong stem structure',
            'Normal flowering if applicable',
            'No leaf lesions or discoloration',
            'Vigorous growth pattern'
        ],
        'causes': [
            'Optimal growing conditions',
            'Proper soil preparation and fertility',
            'Good water management',
            'Effective disease prevention',
            'Quality seed potatoes'
        ],
        'organic_treatments': [
            'Continue current management practices',
            'Regular monitoring for changes',
            'Maintain proper hilling',
            'Practice preventive measures',
            'Ensure adequate nutrition'
        ],
        'supplements': [
            {
                'name': 'Balanced NPK Fertilizer',
                'usage': 'Apply based on soil test recommendations',
                'benefits': 'Supports healthy growth and tuber development'
            },
            {
                'name': 'Organic Compost',
                'usage': 'Work into soil before planting',
                'benefits': 'Improves soil structure and provides nutrients'
            },
            {
                'name': 'Sulfur',
                'usage': 'Apply if soil pH needs adjustment',
                'benefits': 'Maintains optimal soil pH for potato growth'
            },
            {
                'name': 'Bone Meal',
                'usage': 'Apply at planting time',
                'benefits': 'Provides phosphorus for root development'
            }
        ],
        'prevention': [
            'Continue excellent care practices',
            'Regular field scouting',
            'Proper hill maintenance',
            'Good crop rotation practices',
            'Monitor soil moisture levels'
        ]
    },

    # Additional Tomato diseases
    'Tomato_Late_blight': {
        'name': 'Late Blight',
        'plant': 'Tomato',
        'severity': 'Severe',
        'description': 'A highly destructive disease that can rapidly destroy tomato plants and fruit under favorable conditions.',
        'symptoms': [
            'Water-soaked lesions on leaves turning brown',
            'White moldy growth on leaf undersides',
            'Brown, firm lesions on fruit',
            'Blackening of stems and petioles',
            'Rapid plant death in humid conditions'
        ],
        'causes': [
            'Oomycete pathogen Phytophthora infestans',
            'Cool, wet weather (60-70°F)',
            'High humidity and leaf wetness',
            'Poor air circulation',
            'Infected transplants or nearby potatoes'
        ],
        'organic_treatments': [
            'Apply copper fungicides preventively',
            'Remove infected plants immediately',
            'Improve air circulation and drainage',
            'Use resistant varieties when available',
            'Practice strict garden sanitation'
        ],
        'supplements': [
            {
                'name': 'Copper Fungicide',
                'usage': 'Apply before disease onset, weekly during outbreaks',
                'benefits': 'Protects healthy tissue from infection'
            },
            {
                'name': 'Chlorothalonil',
                'usage': 'Apply according to label during favorable conditions',
                'benefits': 'Broad-spectrum protectant fungicide'
            },
            {
                'name': 'Potassium Bicarbonate',
                'usage': '1 tablespoon per gallon water, spray weekly',
                'benefits': 'Alters leaf surface pH to inhibit disease'
            },
            {
                'name': 'Compost Extract',
                'usage': 'Apply as foliar spray and soil drench',
                'benefits': 'Provides beneficial microorganisms'
            }
        ],
        'prevention': [
            'Choose resistant tomato varieties',
            'Ensure good air circulation',
            'Water at soil level, not on leaves',
            'Remove lower leaves touching soil',
            'Monitor weather conditions for disease risk'
        ]
    },

    'Tomato_Leaf_Mold': {
        'name': 'Leaf Mold',
        'plant': 'Tomato',
        'severity': 'Moderate',
        'description': 'A fungal disease that primarily affects greenhouse and high-humidity tomato production.',
        'symptoms': [
            'Yellow spots on upper leaf surface',
            'Olive-green to brown fuzzy growth on leaf undersides',
            'Leaves eventually turn brown and drop',
            'Reduced photosynthesis and fruit quality',
            'Premature defoliation in severe cases'
        ],
        'causes': [
            'Fungal pathogen Passalora fulva (Fulvia fulva)',
            'High humidity (85% or higher)',
            'Poor air circulation',
            'Temperatures between 70-80°F',
            'Overhead watering or condensation'
        ],
        'organic_treatments': [
            'Improve air circulation and ventilation',
            'Reduce humidity levels in growing area',
            'Remove infected leaves immediately',
            'Apply sulfur-based fungicides',
            'Water at soil level only'
        ],
        'supplements': [
            {
                'name': 'Sulfur Fungicide',
                'usage': 'Apply weekly during humid conditions',
                'benefits': 'Prevents spore germination and fungal growth'
            },
            {
                'name': 'Neem Oil',
                'usage': 'Spray every 7-14 days as preventive measure',
                'benefits': 'Natural fungicide with low toxicity'
            },
            {
                'name': 'Baking Soda Solution',
                'usage': '1 tsp per quart water, spray weekly',
                'benefits': 'Changes leaf surface pH to inhibit fungus'
            },
            {
                'name': 'Potassium Silicate',
                'usage': 'Apply as foliar spray bi-weekly',
                'benefits': 'Strengthens plant cell walls against pathogens'
            }
        ],
        'prevention': [
            'Provide excellent air circulation',
            'Control humidity levels below 85%',
            'Space plants properly',
            'Use drip irrigation systems',
            'Choose resistant varieties when available'
        ]
    },

    'Tomato_Septoria_leaf_spot': {
        'name': 'Septoria Leaf Spot',
        'plant': 'Tomato',
        'severity': 'Moderate',
        'description': 'A common fungal disease that causes characteristic small spots with dark borders on tomato leaves.',
        'symptoms': [
            'Small, circular spots with gray centers',
            'Dark brown to black borders around spots',
            'Tiny black specks (pycnidia) in spot centers',
            'Lower leaves affected first',
            'Progressive defoliation from bottom up'
        ],
        'causes': [
            'Fungal pathogen Septoria lycopersici',
            'Warm, humid weather conditions',
            'Rain splash and overhead watering',
            'Poor air circulation',
            'Infected plant debris'
        ],
        'organic_treatments': [
            'Remove infected lower leaves',
            'Apply copper-based fungicides',
            'Improve air circulation',
            'Mulch around plants to prevent soil splash',
            'Water at soil level'
        ],
        'supplements': [
            {
                'name': 'Copper Sulfate',
                'usage': 'Apply every 7-14 days during wet periods',
                'benefits': 'Protects new growth from infection'
            },
            {
                'name': 'Chlorothalonil',
                'usage': 'Apply preventively before disease appears',
                'benefits': 'Broad-spectrum fungicide for leaf spots'
            },
            {
                'name': 'Organic Mulch',
                'usage': 'Apply 2-3 inches around plant base',
                'benefits': 'Prevents soil splash and retains moisture'
            },
            {
                'name': 'Compost',
                'usage': 'Work into soil before planting',
                'benefits': 'Improves soil health and plant resistance'
            }
        ],
        'prevention': [
            'Rotate crops annually',
            'Space plants for good air circulation',
            'Remove plant debris at season end',
            'Avoid overhead irrigation',
            'Choose resistant varieties when available'
        ]
    },

    'Tomato_Spider_mites_Two_spotted_spider_mite': {
        'name': 'Two-spotted Spider Mite Damage',
        'plant': 'Tomato',
        'severity': 'Moderate to Severe',
        'description': 'Damage caused by two-spotted spider mites, tiny arachnids that feed on plant juices causing stippling and webbing.',
        'symptoms': [
            'Fine stippling or speckling on leaves',
            'Yellow or bronze discoloration of leaves',
            'Fine webbing on leaves and stems',
            'Premature leaf drop',
            'Reduced plant vigor and fruit quality'
        ],
        'causes': [
            'Two-spotted spider mites (Tetranychus urticae)',
            'Hot, dry weather conditions',
            'Low humidity levels',
            'Dusty conditions',
            'Overuse of broad-spectrum insecticides'
        ],
        'organic_treatments': [
            'Increase humidity around plants',
            'Spray with strong water to dislodge mites',
            'Apply insecticidal soap or neem oil',
            'Release beneficial predatory mites',
            'Remove heavily infested leaves'
        ],
        'supplements': [
            {
                'name': 'Neem Oil',
                'usage': 'Spray every 3-5 days until control achieved',
                'benefits': 'Suffocates mites and disrupts reproduction'
            },
            {
                'name': 'Insecticidal Soap',
                'usage': 'Apply thoroughly to leaf undersides',
                'benefits': 'Safe, effective contact miticide'
            },
            {
                'name': 'Predatory Mites',
                'usage': 'Release when mite populations are detected',
                'benefits': 'Biological control of spider mites'
            },
            {
                'name': 'Horticultural Oil',
                'usage': 'Apply during cooler parts of day',
                'benefits': 'Smothers mites and eggs'
            }
        ],
        'prevention': [
            'Maintain adequate soil moisture',
            'Provide good air circulation',
            'Avoid excessive nitrogen fertilization',
            'Regular monitoring for early detection',
            'Conserve beneficial insects'
        ]
    },

    'Tomato__Target_Spot': {
        'name': 'Target Spot',
        'plant': 'Tomato',
        'severity': 'Moderate',
        'description': 'A fungal disease causing characteristic target-like lesions on tomato leaves, stems, and fruit.',
        'symptoms': [
            'Small brown spots with concentric rings',
            'Target-like appearance of lesions',
            'Spots may have yellow halos',
            'Lesions can appear on fruit as dark, sunken areas',
            'Defoliation in severe infections'
        ],
        'causes': [
            'Fungal pathogen Corynespora cassiicola',
            'Warm, humid weather conditions',
            'Poor air circulation',
            'Extended periods of leaf wetness',
            'Infected plant debris'
        ],
        'organic_treatments': [
            'Remove infected plant material',
            'Apply copper-based fungicides',
            'Improve air circulation',
            'Practice crop rotation',
            'Use disease-free seeds and transplants'
        ],
        'supplements': [
            {
                'name': 'Copper Hydroxide',
                'usage': 'Apply every 7-14 days during favorable conditions',
                'benefits': 'Protective fungicide against target spot'
            },
            {
                'name': 'Azoxystrobin',
                'usage': 'Apply at first sign of disease',
                'benefits': 'Systemic fungicide with curative properties'
            },
            {
                'name': 'Organic Mulch',
                'usage': 'Apply around plants to prevent soil splash',
                'benefits': 'Reduces disease pressure from soil-borne spores'
            },
            {
                'name': 'Calcium Supplement',
                'usage': 'Apply during fruit development',
                'benefits': 'Strengthens cell walls against fungal invasion'
            }
        ],
        'prevention': [
            'Practice 2-3 year crop rotation',
            'Ensure proper plant spacing',
            'Remove crop debris at season end',
            'Water at soil level, avoid wetting foliage',
            'Choose resistant varieties when available'
        ]
    },

    'Tomato__Tomato_YellowLeaf__Curl_Virus': {
        'name': 'Tomato Yellow Leaf Curl Virus',
        'plant': 'Tomato',
        'severity': 'Severe',
        'description': 'A viral disease transmitted by whiteflies that causes severe yield losses in tomato crops.',
        'symptoms': [
            'Upward curling and yellowing of leaves',
            'Stunted plant growth',
            'Reduced fruit set and size',
            'Interveinal yellowing of leaves',
            'Overall plant decline'
        ],
        'causes': [
            'Tomato Yellow Leaf Curl Virus (TYLCV)',
            'Transmitted by silverleaf whitefly',
            'Hot, dry weather favors whitefly populations',
            'Infected transplants or nearby infected plants',
            'No cure once plant is infected'
        ],
        'organic_treatments': [
            'Control whitefly populations',
            'Remove and destroy infected plants',
            'Use reflective mulches',
            'Apply insecticidal soaps for whitefly control',
            'Practice strict sanitation'
        ],
        'supplements': [
            {
                'name': 'Yellow Sticky Traps',
                'usage': 'Place around plants to monitor and trap whiteflies',
                'benefits': 'Helps detect and reduce whitefly populations'
            },
            {
                'name': 'Neem Oil',
                'usage': 'Apply regularly to control whitefly nymphs',
                'benefits': 'Disrupts whitefly development and feeding'
            },
            {
                'name': 'Reflective Mulch',
                'usage': 'Use silver or aluminum mulch around plants',
                'benefits': 'Confuses and repels whiteflies'
            },
            {
                'name': 'Beneficial Insects',
                'usage': 'Release Encarsia or other whitefly parasitoids',
                'benefits': 'Biological control of whitefly populations'
            }
        ],
        'prevention': [
            'Use virus-resistant tomato varieties',
            'Control whitefly populations early',
            'Use physical barriers like row covers',
            'Remove weeds that harbor whiteflies',
            'Quarantine new plants before introducing to garden'
        ]
    },

    'Tomato__Tomato_mosaic_virus': {
        'name': 'Tomato Mosaic Virus',
        'plant': 'Tomato',
        'severity': 'Moderate to Severe',
        'description': 'A viral disease causing mottled patterns on leaves and reduced fruit quality in tomato plants.',
        'symptoms': [
            'Mosaic pattern of light and dark green on leaves',
            'Mottled or streaked fruit',
            'Stunted plant growth',
            'Distorted leaf shape',
            'Reduced fruit yield and quality'
        ],
        'causes': [
            'Tomato Mosaic Virus (ToMV)',
            'Transmitted through contaminated tools, hands, or clothes',
            'Can survive in plant debris and seeds',
            'Spread by mechanical transmission',
            'No insect vector required'
        ],
        'organic_treatments': [
            'Remove and destroy infected plants',
            'Disinfect tools and hands regularly',
            'Use virus-free seeds and transplants',
            'Practice strict sanitation',
            'Avoid tobacco products around plants'
        ],
        'supplements': [
            {
                'name': '10% Bleach Solution',
                'usage': 'Disinfect tools between plants',
                'benefits': 'Prevents mechanical transmission of virus'
            },
            {
                'name': 'Powdered Milk Spray',
                'usage': 'Mix 1:10 with water, spray on tools',
                'benefits': 'Alternative disinfectant for virus prevention'
            },
            {
                'name': 'Certified Disease-Free Seeds',
                'usage': 'Always use certified virus-free planting material',
                'benefits': 'Prevents introduction of virus to garden'
            },
            {
                'name': 'Beneficial Bacteria',
                'usage': 'Apply to boost plant health and resistance',
                'benefits': 'May help plants tolerate virus infection'
            }
        ],
        'prevention': [
            'Use resistant tomato varieties when available',
            'Practice good sanitation habits',
            'Disinfect tools frequently',
            'Avoid smoking or using tobacco around plants',
            'Remove infected plants immediately'
        ]
    }
}

def get_disease_info(disease_name):
    """Get disease information for a given disease name"""
    return DISEASE_INFO.get(disease_name, {
        'name': 'Unknown Disease',
        'plant': 'Unknown',
        'severity': 'Unknown',
        'description': 'No information available for this condition.',
        'symptoms': [],
        'causes': [],
        'organic_treatments': [],
        'supplements': [],
        'prevention': []
    })

def get_severity_color(severity):
    """Get color class for severity level"""
    severity_colors = {
        'Healthy': 'success',
        'Low': 'info',
        'Moderate': 'warning',
        'Moderate to Severe': 'warning',
        'Severe': 'danger',
        'Unknown': 'secondary'
    }
    return severity_colors.get(severity, 'secondary')

def format_disease_name(raw_name):
    """Format raw disease name to match database keys"""
    # This function can be used to normalize disease names from the model
    return raw_name.replace(' ', '_').replace('-', '_')
