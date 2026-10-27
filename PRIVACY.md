# Cookery privacy policy

Cookery is a cooking skill and camera capture script for Codex on macOS. It does not operate a separate server, create a Cookery account, or include analytics.

## Camera images and conversation

When you start a cooking session, the script saves screenshots of the selected QuickTime camera window, with timestamped filenames, in a folder on your Mac. Images may include people and anything visible in the camera view. They are used to help Codex understand your cooking progress.

Saving a screenshot does not itself send it to Cookery's publisher. When Codex opens an image for analysis, that image is provided to the model service handling your Codex session. Your cooking messages, voice, and any images used in the conversation are handled under your OpenAI account settings and the applicable [OpenAI privacy policy](https://openai.com/policies/privacy-policy/). Deleting local screenshots does not delete conversation history or copies already processed by that service.

## Retention and control

The capture script runs until stopped. Local images remain until you delete them or macOS removes the temporary folder. At the end of a session, the skill instructs Codex to stop capturing and ask before deleting that session's capture folder. You can request that images be kept, stop capture at any time, or delete the folder yourself.

## Support

If you post on [GitHub Issues](https://github.com/rrwwee/cookery/issues), the information you submit is public and is handled by GitHub under its policies. Do not include private camera images, credentials, or other sensitive information in an issue.

Cookery's publisher receives only information you choose to share, such as support issues. Cookery does not independently sell camera images or conversation data.
