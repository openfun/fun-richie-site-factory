terraform {
  required_providers {
    scaleway = {
      source = "scaleway/scaleway"
    }
  }
  required_version = ">=1.6.1"

  backend "s3" {
    bucket                      = "richie-site-factory-terraform"
    key                         = "terraform.tfstate"
    endpoint                    = "https://s3.fr-par.scw.cloud"
    region                      = "fr-par"
    skip_credentials_validation = true
    skip_region_validation      = true
    skip_requesting_account_id  = true
    encrypt                     = true
    use_lockfile                = true
  }
}

provider "scaleway" {
  zone = var.scw_zone
  region = var.scw_region
  project_id = var.scw_project_id
  organization_id = var.scw_organization_id
}
