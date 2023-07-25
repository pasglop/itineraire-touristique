from ..v1.itinary.itinary import ItinaryStepVisitSchema, ItinaryStepWalkSchema, VisitDetailSchema, WalkDetailSchema
from ..v1.poi import poi_detail_example


def test_itinary_step_visit_schema():
    poi = poi_detail_example
    step_detail = VisitDetailSchema(**poi)
    itinary_step = ItinaryStepVisitSchema(
        step=1,
        name=poi['name'],
        step_detail=step_detail,
        instruction='Visiter',
        comment='Commentaire'
    )
    assert itinary_step.step_type == 'Visiter'
    assert itinary_step.step_detail.name == 'Tour Eiffel'

def test_itinary_step_walk_schema():
    walk_detail = WalkDetailSchema(
        name='Marcher vers la tour Eiffel',
        distance=1000,
        duration=10,
        start_latitude=48.85836,
        start_longitude=2.294543,
        end_latitude=48.85836,
        end_longitude=2.294543
    )
    itinary_step = ItinaryStepWalkSchema(
        step=1,
        name='Marcher vers la tour Eiffel',
        step_detail=walk_detail,
        instruction='Marcher',
        comment='Commentaire'
    )
    assert itinary_step.step_type == 'Marcher'
    assert itinary_step.step_detail.duration == 10

