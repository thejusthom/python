i = 1
intervals = [[2,6],[1,3],[8,10],[15,18]]
intervals.sort(key=lambda interval:interval[0])
output_list = []
while i < len(intervals):
    print(intervals[-1][1])
    startPrev = intervals[i-1][0]
    endPrev = intervals[i-1][1]
    start = intervals[i][0]
    end = intervals[i][1]
    if endPrev >= start:
        output_list.append([min(startPrev,start),max(endPrev,end)])
    else:
        output_list.append([startPrev,endPrev])
        output_list.append([start,end])
    i += 2
for op in output_list:
    print(op[0])
    print(op[1])