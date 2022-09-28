## Checkmarx Supply Chain Security(SCS) API Github Action


Simple Github Action to call the Checkmarx Supply Chain Security API

### What you will need to use this Github Action
- The Checkmarx SCS API
- A Checkmarx SCS API Token *(contact your Checkmarx representative for this information, don't have Checkmarx, [Try a free trial today!](https://info.checkmarx.com/ast-free-trial?utm_source=cxsean_github&utm_medium=scm&utm_campaign=free_trial_from_cxsean&utm_id=cxonefreetrial)*
)

### Additional Information
Simple Github Action to call the Checkmarx SCS api.  Currently only looking for NPM packages and using the package.json as the manifest file. The script takes the dependencies json from the package.json and converts it into an acceptable format for the body of the api request.

User can define:
- The path of the package.json
- The path and name of the results file(must be a .json to work properly.

### Known Issues
"*It's a feature, not a bug*" ¯\_(ツ)_/¯ - The Github Action will fail if there are no changes to the results file.

### Future updates: 
Hoping to include other manifest files and also include html and pdf options!