.. title:: Home

.. raw:: html

    <div class="row">
        <div class="col-md-12">
            <p>Did you ever want to test your payload against all requests of a certain domain? N.Y.A.W.C can help you with that. It crawls all requests (e.g. GET, POST or PUT) on the specified domain and keeps track of the request and response data. During the crawling process, the callbacks enable you to insert your payload at specific places and test if they worked. And using the built in options you can do even more. <a href="getting_started.html">Get started</a>!</p>
        </div>
    </div>
    <hr>
    <div class="row">
        <div class="col-md-3">
            <strong>Step #1</strong>
            <p>You can define your startpoint (a request) and the crawling scope and then start the crawler.</p>
        </div>
        <div class="col-md-3">
            <strong>Step #2</strong>
            <p>The crawler repeatedly starts the first request in the queue until <code>max threads</code> is reached.</p>
        </div>
        <div class="col-md-3">
            <strong>Step #3</strong>
            <p>The crawler adds all requests found in the response to the end of the queue (except duplicates).</p>
        </div>
        <div class="col-md-3">
            <strong>Step #4</strong>
            <p>The crawler goes back to step #2 to spawn new requests repeatedly until <code>max threads</code> is reached.</p>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12 text-center">
            <img src="_static/img/flow.svg" class="flow img-responsive" />
        </div>
    </div>
    <div class="row">
        <div class="col-md-12 text-center">
            <p>Several <a href="options_callbacks.html">callbacks</a> can be used throughout the crawling process to, for example, modify requests on the go.</p>
        </div>
    </div>
