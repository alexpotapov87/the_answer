from ..api import api
from ..main import app
from flask import Flask, render_template, request, redirect
from prometheus_flask_exporter import PrometheusMetrics


metrics = PrometheusMetrics(app)


metrics.info('app_info', 'Application info', version='1.0.3')


@app.route("/")
def root():
    return render_template('base.html')


@app.route('/skip')
@metrics.do_not_track()
def skip():
    pass  # default metrics are not collected


@app.route('/<item_type>')
@metrics.do_not_track()
@metrics.counter('invocation_by_type', 'Number of invocations by type',
                 labels={'item_type': lambda: request.view_args['type']})
def by_type(item_type):
    pass  # only the counter is collected, not the default metrics


@app.route('/long-running')
@metrics.gauge('in_progress', 'Long running requests in progress')
def long_running():
    pass


@app.route('/status/<int:status>')
@metrics.do_not_track()
@metrics.summary('requests_by_status', 'Request latencies by status',
                 labels={'status': lambda r: r.status_code})
@metrics.histogram('requests_by_status_and_path', 'Request latencies by status and path',
                   labels={'status': lambda r: r.status_code, 'path': lambda: request.path})
def echo_status(status):
    return 'Status: %s' % status, status
