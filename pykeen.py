import torch
from pykeen.triples import TriplesFactory
from pykeen.pipeline import pipeline
from pykeen.datasets import get_dataset
from pykeen.predict import predict_triples

# Load your dataset (replace 'db100k' with the actual dataset name)
dataset = get_dataset(dataset='DB100k')



# Access training triples
training_triples = dataset.training.triples

# Create a TriplesFactory
triples_factory = TriplesFactory.from_labeled_triples(training_triples, create_inverse_triples=True)

# Split the dataset into training and testing
training, testing = dataset.training, dataset.testing

# Train a model on the dataset
result = pipeline(
    training=training,
    testing=testing,
    model='rescal',
    training_loop='sLCWA',
    epochs=5,
    device='cuda',  # Use GPU acceleration
    training_kwargs=dict(batch_size=128),  # Adjust batch size
)

# Access the trained model from the result
trained_model = result.model

# Entity and relation of interest
head_entity = 'Barack_Obama'
relation = 'isMarriedTo'  # Replace with the relation of interest in your dataset

# Convert entities and relation to indices
head_entity_idx = dataset.entity_to_id.get(head_entity)
relation_idx = dataset.relation_to_id.get(relation)

# Check if entities and relation are found in mappings
if head_entity_idx is not None and relation_idx is not None:
    # Generate triples for scoring (with a placeholder for tail entity)
    tail_entity_candidates_idx = range(trained_model.num_entities)
    triples_to_score = torch.tensor([
        (head_entity_idx, relation_idx, tail_entity_idx)
        for tail_entity_idx in tail_entity_candidates_idx
    ])

    # Score the triples using the model and the new TriplesFactory
    scores = predict_triples(model=trained_model, triples=triples_to_score, triples_factory=triples_factory)

    # Find the highest-scoring triple
    best_index = torch.argmax(scores)
    best_tail_entity_idx = triples_to_score[best_index][2]
    best_tail_entity = triples_factory.id_to_entity[best_tail_entity_idx]

    print(f"Predicted tail entity: {best_tail_entity}")
else:
    print(f"Entity '{head_entity}' or relation '{relation}' not found in mappings.")