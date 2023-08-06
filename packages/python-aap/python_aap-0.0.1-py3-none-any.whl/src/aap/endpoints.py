import os
import datetime

import base
import mixins


class Schedule(base.APIObject):
    _path = 'schedules/'
    _action = {}
    _map = {
        'dtstart': lambda x: datetime.datetime.fromisoformat(x.replace("Z", "")),  # unsuported ISO format until 3.11
        'dtend': lambda x: datetime.datetime.fromisoformat(x.replace("Z", ""))   # unsuported ISO format until 3.11
    }

base.__schedule_class = Schedule


class JobEvent(base.APIObject):
    _display = "event"

class Job(base.APIObject, mixins.WaitableMixin):
    _path = 'jobs/'
    _sub = {
        'job_events': JobEvent
    }
    @property
    def artifacts(self):
        if self.status not in self._states:
            return None
        for event in self.job_events:
            if event.event == "playbook_on_stats":
                return event.get('artifact_data', {})
    @property
    def web_url(self):
        return os.path.join(self.api.url.strip(self.api.vstr) +f"/#/jobs/playbook/{self.id}/details")

class WorkflowNode(base.APIObject):
    _path = "workflow_nodes"
    _related = {
        'job': base.Related(Job, 'summary_fields', 'job', 'id', iterable=False, prefix='jobs/')
    }
    @property
    def is_executed(self):
        return self._data.get('job') is not None
class WorkflowJob(base.APIObject, mixins.WaitableMixin):
    _path = 'workflow_jobs/'
    _related = {
        'workflow_nodes': base.Related(WorkflowNode, 'related', 'workflow_nodes', iterable=True)
    }
    @property
    def web_url(self):
        return os.path.join(self.api.url.strip(self.api.vstr) +f"/#/jobs/workflow/{self.id}/output")

    def job_nodes(self):
        for workflow_node in self.workflow_nodes:
            if workflow_node._data.get('summary_fields', {}).get('job', {}).get('type') == 'job':
                yield workflow_node

class WorkflowJobTemplate(base.APIObject, mixins.LaunchableMixin):
    _creates = WorkflowJob
    _related = {

    }
    _sub = {
        'workflow_jobs': WorkflowJob,
        'schedules': Schedule
    }
    _path = 'workflow_job_templates/'
    @property
    def web_url(self):
        return os.path.join(self.api.url.strip(self.api.vstr) +f"/#/templates/workflow_job_template/{self.id}/details")


class JobTemplate(base.APIObject, mixins.LaunchableMixin):
    _creates = Job
    _related = {

    }
    _sub = {
        'jobs': Job,
        'schedules': Schedule
    }
    _path = 'job_templates/'
    @property
    def web_url(self):
        return os.path.join(self.api.url.strip(self.api.vstr) +f"/#/templates/job_template/{self.id}/details")


class Organization(base.APIObject):
    _related = {

    }
    _sub = {
        'workflow_job_templates': WorkflowJobTemplate,
        'job_templates': JobTemplate
    }
    _path = 'organizations/'

class Group(base.APIObject):
    _path = "groups/"

class Host(base.APIObject):
    _path = "hosts/"

class Inventory(base.APIObject):
    _path='inventories/'
    _sub = {
        'hosts': Host,
        'groups': Group
    }
