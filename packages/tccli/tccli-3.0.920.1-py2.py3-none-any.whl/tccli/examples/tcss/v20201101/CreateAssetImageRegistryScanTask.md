**Example 1: 镜像仓库创建镜像扫描任务**



Input: 

```
tccli tcss CreateAssetImageRegistryScanTask --cli-unfold-argument  \
    --Id 8741110 \
    --ScanType CVE VIRUS RISK
```

Output: 
```
{
    "Response": {
        "RequestId": "68d5d49c-4b6b-46af-b060-46f521db0400"
    }
}
```

