
# CHANGELOG

## v0.7.0

* feature: Add VolumeAttached waiter (#55 by tunakyonn)
* feature: Update computing model for add live migration api (#54 by miyuush)

## v0.6.0

* fix: Fix computing model json for typo (#52 by fuku2014, #53 by tunakyonn)

## v0.5.0

* feature: Update computing model for remove rip api (#51 by fuku2014)
* feature: Update rdb model for fixed bug (#51 by fuku2014)

## v0.4.0

* feature: Update rdb model json for add ModifyDBInstanceNetwork (#50 by fuku2014)
* fix: Fix computing waiter json for add elb error code. (#49 by fuku2014)

## v0.3.1

* feature: Migrating from Travis CI to GitHub Actions. (#48 by aokumasan)
* feature: Update to latest computing JSON. (#47 by aokumasan)

## v0.3.0

* feature: Update model (#46 by fuku2014)
* feature: Add rdb and nas protocol for date (#44 by tunakyonn)
* feature: Add support userdata encoding (#39 by fuku2014)

## v0.2.3

* fix: Add `Description` field to DescribeVolumes response (#36 by tily)
* fix: Remove unnecessary field (#36 by tily)

## v0.2.2

* fix: Fix modify / reset db-parameter-group bug (#35 by tily)
* fix: Fix upload-ssl-certificate bug (#34 by tily)
* fix: Fix help text on CLI parameter error  (#33 by tily)
* fix: Fix CLI command name (#32 by tily)

## v0.2.1

* feature: Add APIs and fix some bugs (#31 by tily)
    * Added APIs
        * computing:CopyFromBackupInstance
        * computing:CreateBackupInstances
        * computing:CreateInstanceBackupRule
        * computing:DeleteInstanceBackupRule
        * computing:DescribeInstanceBackupRuleActivities
        * computing:DescribeInstanceBackupRules
        * computing:ModifyInstanceBackupRuleAttribute
        * computing:NiftyAssociateRouteTableWithElasticLoadBalancer
        * computing:NiftyDescribeLoadBalancerSSLPolicies
        * computing:NiftyDisassociateRouteTableFromElasticLoadBalancer
        * computing:NiftyReplaceElasticLoadBalancerListenerSSLCertificate
        * computing:NiftyReplaceRouteTableAssociationWithElasticLoadBalancer
        * computing:NiftySetLoadBalancerSSLPoliciesOfListener
        * computing:NiftyUnsetLoadBalancerSSLPoliciesOfListener
        * computing:RefreshInstanceBackupRule
        * computing:SetLoadBalancerListenerSSLCertificate
        * computing:UnsetLoadBalancerListenerSSLCertificate
        * nas:ClearNASSession
        * rdb:DescribeCertificates
        * rdb:ResetExternalMaster
        * rdb:SetExternalMaster
        * rdb:StartReplication
        * rdb:StopReplication
    * Fixed some bugs


## v0.2.0

* feature: Support Hatoba beta (#30 by alice02)

## v0.1.9

* fix: Fix bug of cannot parse the DescribeDhcpOptions response (#29 by alice02)

## v0.1.8

* fix: Override config load path (#28 by alice02)

## v0.1.7

* fix: Update requires dist (#27 by alice02)
* fix: update dependencies to fix vulnerability (#26 by alice02)
* fix: service-2.json for computing (#25 by sato-mh)
* feature: Add serviceId to models (#24 by alice02)
* fix: dependency for requests (#23 by sato-mh)
* feature: Add markdown support for pypi long description (#22 by tottoto)
* feature: update version of dependency libraries (#21 by sato-mh)

## v0.1.6


* fix: botocore and awscli versions in `setup.*` (#19 by @tily)
* feature: Support Computing Network Interface API (#18 by @alice02)
* fix: Modify nifcloud-debugcli to support new version of awscli (#17 by @sato-mh)
* fix: Fix version of some dependencies for development (#16 by @alice02)
* fix: Modify to new endpoints (#15 by @sato-mh)
* fix: Fix Ca parameter of UploadSslCertificate in computing (#14 by @yoshd)

## v0.1.5

* fix: fix #11, and add location names for other SDKs (#12 by @tily)
* fix: Fixed version of the following dependencies: botocore and awscli (#10 by @alice02)
* feature: Add `register_add_waiters` handler to support wait command of nifcloud-debugcli (#8 by @alice02)

## v0.1.4

* feature: Add computing instance waiters (#7 by @tily)
* fix: Use pipenv scripts (#6 by @sato-mh)
* feature: Add script for uploading to pypi (#5 by @sato-mh) 

## v0.1.3

* feature: Update computing and rdb model JSON. (#3 by @alice02)

## v0.1.2

* feature: Parse global args like `--query`. (#1 by @tily)

## v0.1.1

* feature: Initial import. :tada:
