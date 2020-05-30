import random
from datetime import timedelta

class TelemetryPoint:
    def __init__(self, timestamp, lat, lon):
        self.timestamp = timestamp
        self.lat = lat
        self.lon = lon


class TelemetryTrack:

    def __init__(self, points):
        # Make sure the TelemetryTrack info will be chronological.
        points_chronological = sorted(points, key=lambda point: point.timestamp)

        self.points = points_chronological
        self.timestamps = [point.lat for point in points_chronological]
        self.lats = [point.lat for point in points_chronological]
        self.lons = [point.lon for point in points_chronological]

    def earliest_timestamp(self):
        if not self.timestamps:
            return None
        return self.timestamps[0]

    def latest_timestamp(self):
        if not self.timestamps:
            return None
        return self.timestamps[-1]

    @classmethod
    def make_wandering_track(cls, start_point, step_time_interval=None, step_count=100, step_scale=0.01):
        if step_time_interval is None:
            step_time_interval = timedelta(minutes=1)

        points = [start_point]

        steps = 0
        previous_point = start_point
        while steps < step_count:
            point = TelemetryPoint(
                timestamp=previous_point.timestamp + step_time_interval,
                lat=previous_point.lat + random.uniform(-step_scale, step_scale),
                lon=previous_point.lon + random.uniform(-step_scale, step_scale)
            )
            points.append(point)
            previous_point = point
            steps += 1

        return cls(points)
