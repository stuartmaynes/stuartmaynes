Title: Using Terraform to provision Heroku apps
Category: Terraform
Tags: Heroku, Terraform
Date: 2020-04-19 12:00
Modified: 2020-04-19 17:05
Summary: A look at how to use Terraform to provision Heroku apps with add-ons from the Heroku Marketplace, connected via a pipeline.

<p class="notice">This article assumes that you have installed Terraform, have setup an account with Heroku, and are familiar with the Heroku platform and the command line.</p>

The aim of this article is to guide you through the process of creating a Terraform configuration for Heroku. The configuration will provision two apps, linked via a pipeline, as well as add-ons from the Marketplace. The final configuration can then be used as a template, which you can then tailor to your requirements - automating the process of provisioning an Heroku infrastructure.

## Getting Started

Create a file called `heroku.tf` in a directory of your choice and add the following block.

```terraform
provider "heroku" {
    version = "~>2.0"
}
```

This block specifies Heroku as a provider and sets the required version number to `~>2.0`.  Providers are plugins for Terraform that offer a set of named resources. Named resources are how Terraform interacts with the provider's API. A configuration can have multiple providers, for example, you may also want to use the Amazon Web Services provider.

### Install the provider plugin

On the command line, change directory in the same location as your `heroku.tf` file and run the command below.
```text
$ terraform init
```
Running `terraform init` will create a `.terraform` directory inside your present working directory and install the plugin to it. You should see something similar to the output below.
```text
Initializing provider plugins...
- Checking for available provider plugins...
- Downloading plugin for provider "heroku" (terraform-providers/heroku) 2.3.0...

Terraform has been successfully initialized!
```
### Heroku Authentication

In order to interact with the Platform API we need to provide our Heroku account email address and API key. We can supply these details in one of a few ways:

#### Inside the configuration file

The provider block for Heroku can be given the name and password parameters. The name parameter is your email address and the password is your API key.
```terraform
provider "heroku" {
    version = "~>2.0"
    name = <heroku_account_email>
    password = <heroku_api_key>
}
```
Hardcoding these values in the configuration isn't best practise and should be avoided for security reasons. If these details were to become publicly available, someone could delete all your apps and add-ons 😬.

#### Using a .netrc file

Create a file called `.netrc` in your home directory and add the following code into it, replacing the placeholders with the actual values.
```text
# ~/.netrc
machine api.heroku.com
    login <heroku_account_email>
    password <heroku_api_key>
```
**Note:** if you have previously logged into the Heroku Toolbelt a `.netrc` file will already be present. In this case simply append your credentials to it instead.

#### Using environment variables

The variables can be set on the command line prior to running Terraform commands.
```text
$ export HEROKU_EMAIL=<heroku_account_email>
$ export HEROKU_API_KEY=<heroku_api_key>
```
These variable will only last for the current session, so you may want to add them to your `~/.profile, ~/.bashrc, or ~/.zshrc` file in order for them to persist.

## Resources

A resource is a block that describes one or more infrastructure objects. The `resource` keyword is followed by a `string` for the resource type ("heroku_app") and a `string` for the given local name ("staging"). The local name is given by you and it's what you use to refer to the block from elsewhere within the configuration.
```terraform
resource "heroku_app" "staging" {
    name   = "my-staging-app"
    region = "eu"
}
```
The resource block above specifies a Heroku app called staging, with the required `name` and `region` arguments.

### Staging and production apps

Add a second resource block to define the production app. Multiple `heroku_app` resources can be defined within the same configuration file, as long as the given name for each block (of the same type) is different.
```terraform
# Create a staging app
resource "heroku_app" "staging" {
    name   = "my-app-staging"
    region = "eu"
}
# Create a production app
resource "heroku_app" "production" {
    name   = "my-app-production"
    region = "eu"
}
```
## Provisioning two apps linked by a pipeline

Add the following three blocks to your configuration file to create a pipeline and "couple" the two apps to it.
```terraform
# Create the pipeline
resource "heroku_pipeline" "pipeline" {
    name = "my-app-pipeline"
}
# Couple the staging app to the pipeline
resource "heroku_pipeline_coupling" "staging" {
    app      = heroku_app.staging.name
    pipeline = heroku_pipeline.pipeline.id
    stage    = "staging"
}
# Couple the production app to the pipeline
resource "heroku_pipeline_coupling" "production" {
    app      = heroku_app.production.name
    pipeline = heroku_pipeline.pipeline.id
    stage    = "production"
}
```
A resource `heroku_pipeline` block is used first to create a pipeline with the name "my-app-pipeline". Two `heroku_pipeline_coupling` resources are used next to connect the two apps to the pipeline. A `heroku_pipeline_coupling` has both an `app` and `pipeline` parameter, the values of which refer to other resources using dot notation. The dot notation is made up of three parts `<resource_type>.<given_name>.<parameter>`.

## Using Terraform

In this section we are going to use the `plan`, `apply` and `destroy` commands to interact with the Heroku API.

### Plan

The `plan` command creates an execution plan. Execution plans are used to determine what actions are needed to achieve the configuration set out in the `.tf` file. Use `plan` to ensure the changes that will be made match what you expect.
```text
$ terraform plan
```
Running `terraform plan` will produce a diff, of which there is a snippet below. The presence of a `+` indicates an addition, a `~` represents a change, and `-` represents a removal. At this stage you should see a `+` for all resources.
```text
# heroku_pipeline.pipeline will be created
    + resource "heroku_pipeline" "pipeline" {
        + id   = (known after apply)
        + name = "my-app-pipeline"
    }
```
### Apply

The `apply` command is used to make the changes set out in the configuration file.
```
$ terraform apply
```
An output similar to the one `plan` generates will be displayed in your terminal. This time however, Terraform will pause for input.
```text
Plan: 5 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
    Terraform will perform the actions described above.
    Only 'yes' will be accepted to approve.
```
Answering `yes` at this stage will cause the Heroku apps and pipeline to be provisioned. You should see an output like the following.
```text
heroku_app.production: Creating...
heroku_app.staging: Creating...
heroku_pipeline.pipeline: Creating...
heroku_pipeline.pipeline: Creating... complete after 1s
heroku_app.staging: Creation complete after 7s
heroku_pipeline_coupling.staging: Creating...
heroku_app.production: Creation complete after 7s
heroku_pipeline_coupling.production: Creating...
heroku_pipeline_coupling.staging: Creation complete after 2s
heroku_pipeline_coupling.production: Creation complete after 2s

Apply complete! Resources: 5 added, 0 changed, 0 destroyed.
```
If you login to Heroku now you should be able to see the pipeline with the two apps attached. As an alternative, if you have the Heroku Toolbelt installed, try `heroku apps` and the apps should be listed in the output.

#### Error name is already taken

You may get an error from the Heroku API informing you that the name of an app is already taken.
```text
Error: Post https://api.heroku.com/apps: Name my-app-staging is already taken
```
The solution to this is to rename the app or apps within the resource block. Heroku requires all apps on it's infrastructure to be unique.

### Destroy

The `destroy` command is used to destroy the Terraform-managed infrastructure. In our case this will destroy the two apps and the pipeline that we have defined.
```text
$ terraform destroy
```
After running `terraform destroy` you will be shown a diff again, to which you will have to answer `yes` to accept the changes.
```text
...
# heroku_pipeline.pipeline will be destroyed
    - resource "heroku_pipeline" "pipeline" {
        - id   = "256afcc9-9ce3-4b5e-bb51-3ec92444cb17" -> null
        - name = "my-app-pipeline" -> null
    }
...
Plan: 0 to add, 0 to change, 5 to destroy.

Do you really want to destroy all resources?
    Terraform will destroy all your managed infrastructure, as shown above.
    There is no undo. Only 'yes' will be accepted to confirm.

    Enter a value: yes
```
Answering `yes` at this point will start the process of tearing down the infrastructure.
```text
heroku_pipeline_coupling.production: Destroying...
heroku_pipeline_coupling.staging: Destroying...
heroku_pipeline_coupling.production: Destruction complete after 1s
heroku_app.production: Destroying...
heroku_pipeline_coupling.staging: Destruction complete after 1s
heroku_pipeline.pipeline: Destroying...
heroku_app.staging: Destroying...
heroku_pipeline.pipeline: Destruction complete after 0s
heroku_app.production: Destruction complete after 0s
heroku_app.staging: Destruction complete after 0s

Destroy complete! Resources: 5 destroyed.
```
Once complete the two apps and the pipeline have been destroyed and are no longer accessible via the Heroku website or the Heroku Toolbelt.

## Provisioning add-ons

Add-ons from The Heroku Elements Marketplace can be provisioned with the `heroku_addon` resource. Below is an example of attaching a Heroku Redis instance to the staging app, on the hobby-dev (free) plan.
```terraform
# Create and attach a Redis resource to the staging app
resource "heroku_addon" "redis-staging" {
    app  = heroku_app.staging.name
    plan = "heroku-redis:hobby-dev"
}
```
The `app` parameter is the app which you want to attach the resource to. The value follows the same principles mentioned earlier - resource type, followed by the given name for the resource (app), followed by the parameter to reference (name).

The `plan` parameter is made up of the add-ons slug and the plan, separated by a colon. These values are listed on each add-ons page on the market place.

**Note:** provisioning certain add-ons will require billing details to be attached to the account.

## Variables

So far we have hardcoded certain values, such as the name of the apps and the region, that could be replaced with variables. Variables are defined using the `variable` block, the second parameter is the name of the variable. The description parameter is used for documentation and is displayed on the CLI.
```terraform
variable "app_name" {
    description = "Name of the Heroku app provisioned"
}
variable "app_region" {
    description = "Region the app is provisioned in"
}
```
Variables are referenced throughout the configuration, like so
```terraform
var.app_name
var.app_region
```
String interpolation can be done using the following syntax
```terraform
"${var.app_name}-staging"
```
### Using the variables

Update your `heroku.tf` file to use variables for both the app's name and region by first declaring the variable blocks at the top of the file.
```terraform
variable "app_name" {
    description = "Name of the Heroku app provisioned"
}
variable "app_region" {
    description = "Region the app is provisioned in"
}
```
Then update the `heroku_app` and `heroku_pipeline` blocks to use the variables like so.
```terraform
resource "heroku_app" "staging" {
    name   = "${var.app_name}-staging"
    region = var.app_region
}
resource "heroku_app" "production" {
    name   = "${var.app_name}-production"
    region = var.app_region
}
resource "heroku_pipeline" "pipeline" {
    name = var.app_name
}
```
String interpolation is used for the app name to include `staging` and `production` for the staging and production apps respectively.

### Specifying the values

Now when running `terraform apply` or `terraform plan` the CLI will stop and ask for the values for both `app_name` and `app_region`. Example below.
```text
var.app_name
    Name of the Heroku app provisioned

    Enter a value:
```
The values can be provided on the command line using the `-var` option. The `-var` option can be set multiple times.
```text
$ terraform plan -var "app_name=my-startup" -var "app_region=eu"
```
A vars file can be provided using the  `-var-file` option. A vars file has the file type `.tfvars` or `.tfvars.json` and consists only of variable name assignments.
```terraform
app_name = "my-app"
app_region = "eu"
```
If a `.json` file is used the variables have to be declared using the JSON format.
```json
{
    "app_name": "my-app",
    "app_region": "eu"
}
```
If in the directory there is a file called `.auto.tfvars` or `.auto.tfvars.json` then it will automatically be loaded.

#### Defaults

The values can also be set in the block and they are defined using the `default` param. This allows us to set a "default" which can be overwritten via one of the methods mentioned above.
```terraform
variable "app_region" {
    default = "eu"
    description = "Region the app is provisioned in"
}
```
Now that your file is using variables try running `terraform plan` or `terraform apply` to see the difference and make sure it works. Don't forget to run `terraform destroy` if you don't want the infrastructure to persist.

## Conclusion

At this point you should have a Terraform configuration file that provisions two apps as part of a pipeline. If you added any Marketplace add-ons then those too will be provisioned as part of running `terraform apply`. We used variables to keep the file DRY and provide the flexibility to provision other pipelines using the same file. This file can provide the basis for your own requirements. You may want to specify the buildpack, dyno formation, and any environment variables you need.

### Further reading

There is a lot more to Terraform than what was covered above. Below are some links to documentation that will be useful:

- [Terraform CLI documentation](https://www.terraform.io/docs/commands/index.html)
- [Terraform Heroku provider documentation](https://www.terraform.io/docs/providers/heroku/index.html)
- [Using variables with Terraform](https://www.terraform.io/docs/configuration/variables.html)

I've uploaded the [full configuration file](https://github.com/stuartmaynes/terraform-heroku), with a few additions, to [my GitHub profile](https://github.com/stuartmaynes). Please feel free to download it and configure it to your own needs.
