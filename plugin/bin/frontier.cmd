@echo off
if not defined FRONTIER_TOKEN set FRONTIER_TOKEN=unset
"%~dp0mise.cmd" tool-stub "%~dp0frontier.stub" %*
