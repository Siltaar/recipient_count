# recipient\_count
Parse email headers and return the recipient count.

Expect email to be streamed via stdin.

## Environment
Created to be used with [FDM](https://github.com/nicm/fdm) in a `pipe` matching rule.

Now integreated to the larger approach : [py_idempotent_spam_test](https://github.com/Siltaar/py_idempotent_spam_test).

## Example

### Test example :
`echo "To:a@a.tk, b@b.tk" | recipient_count.py`

`2`

### `fdm.conf` example :
`match pipe "python3 -sqI recipient_count.py" returns (,"^[0-9]{2,}$") action maildir "%h/.Maildir/.spam"`
