+++
title = "Passing passwords in Bash without storing them"
date = 2025-08-17

[taxonomies]
tags = ["bash", "tech", "cli"]
+++

Today I learned something cool that I think is worth sharing. I was working on
a script where I needed to make a curl request to acquire a token, for which I
needed to pass my password.

My first instinct was to just put the password in the script, **but then I
might accidentally push the script with my password in it** (I was in a git
repo). So let's not do that. Another option is to simply export it in your bash
session before you execute the script like such:

```bash
export SECRET=my_password && ./my_script.sh

# and then in your script read the password into the $PASSWORD variable
password=$SECRET
```

**The problem with this is that now your password might end up in your shell
history!** You might, like me, have a smart shell history manager like
[Atuin](http://atuin.sh/) that, by default, detects and doesn't save it to your
history. But not everyone does.

Instead, we can ask the user to input their password and pass it to the script
without exposing it in any way.

```bash
( IFS= read -rs -p 'Password: ' pass </dev/tty && MY_PASSWORD="$pass" exec ./my_script.sh )

# and then in your script read the password into the $PASSWORD variable
password=$MY_PASSWORD
```

So what's happening here?
* Subshell `(...)`: Runs in its own shell; **variables die when it exits—no unset needed.**
* `read -rs`:
  * `-r` don’t treat backslashes specially.
  * `-s` silent (no echo) for passwords.
* `IFS=`: Disables trimming/splitting so leading/trailing spaces in the
password aren’t lost.
* `-p 'Password: '`: A prompt for the user
* `</dev/tty`: Reads from the terminal, not stdin—so your script can still use
stdin.
* `MYAPP_PASSWORD="$pass"` cmd: Sets an env var only for that command; avoids a
global export.
* `exec`: Replaces the subshell with your script (no extra process, nothing
runs after). Optional; `./my_script.sh` also works.

This obviously only works for manually executed scripts and not scheduled
ones. I've never seen this before and thought it was pretty clever so I wanted
to share.

