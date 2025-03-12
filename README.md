# BlenderTemplate

This is n example template of an Addon for blender. It uses `venv` to manage a virtual environment, and `pydoctor` for automated API documentation.

Please adjust the `blender_manifests.toml` for your new addon to appear in Blender as a unique Addon.

## Commands

A list of commands to use when developing the Addon

##### Activate the Virtual Environment

Activate this virtual environment so that required packages are tracked to ensure shared workflows between developers building tools

```
scripts\ActivateEnvironment.bat
```

##### Cache the Virtual Environment

```
scripts\CacheEnvironment.bat
```

##### Generate API Documentation

```
scripts\GenerateDocs.bat
```
