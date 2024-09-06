from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment,AssignmentStateEnum

from .schema import AssignmentSchema,AssignmentSubmitSchema,AssignmentGradeSchema

# Create a Blueprint for principal assignments
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)


@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of submitted and graded assignments"""
    # Fetch assignments that are either "SUBMITTED" or "GRADED"
    assignments = Assignment.get_submitted_and_graded_assignments_by_principal(p)
    # Serialize the result using AssignmentSchema
    assignments_dump = AssignmentSchema().dump(assignments, many=True)
    # Return the API response
    return APIResponse.respond(data=assignments_dump)



@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    """Grade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)
    assignment = Assignment.query.get(grade_assignment_payload.id)
    graded_assignment = Assignment.mark_grade_by_principal(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)


@principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of submitted and graded assignments"""
    # Fetch assignments that are either "SUBMITTED" or "GRADED"
    teachers = Assignment.get_all_teachers(p)
    # Serialize the result using AssignmentSchema
    teachers_dump = AssignmentSchema().dump(teachers, many=True)
    # Return the API response
    return APIResponse.respond(data=teachers_dump)

