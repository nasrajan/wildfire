# Fire prediction, detection and spread pattern UI

This UI is based on a fork from the google earth engine demos.
.
To set the app up, follow the instructions in the Developer Docs to
[deploy an EE-based App Engine app](https://developers.google.com/earth-engine/app_engine_intro#deploying-app-engine-apps-with-earth-engine).
For the credentials section, you'll need a Service Account, not an OAuth2 Client
ID. Next:

1.  Move the Service Account private key (`privatekey.json`) into the
    `demos/server-auth-nodejs` folder.
2.  [Create an API key](https://developers.google.com/maps/documentation/javascript/get-api-key)
    and include it in `views/index.hbs` to load Google Maps API.
    
Run : node server.js
