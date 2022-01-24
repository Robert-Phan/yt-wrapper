from dataclasses import dataclass
from utils import camel_snake_converter, assign_resource_dict_to_class
@dataclass
class ThumbnailKey:
    url: str = None
    width: int = None
    height: int = None
    
@dataclass
class Thumbnails:
    default: ThumbnailKey = None
    medium: ThumbnailKey = None
    high: ThumbnailKey = None
    standard: ThumbnailKey = None
    maxres: ThumbnailKey = None
    
@dataclass
class Localized:
    title: str = None
    description: str = None

@dataclass # top-level
class Snippet:
    published_at: str = None
    channel_id: str = None
    title: str = None
    description: str = None
    thumbnails: Thumbnails = None
    channel_title: str = None
    tags: list[str] = None
    category_id: str = None
    live_broadcast_content: str = None
    default_language: str = None
    localized: Localized = None
    
@dataclass
class RegionRestriction:
    allowed: list[str] = None
    blocked: list[str] = None

@dataclass
class ContentRating:
    # jesus christ.
    acb_rating: str = None
    agcom_rating: str = None
    anatel_rating: str = None
    bbfc_rating: str = None
    bfvc_rating: str = None
    bmukk_rating: str = None
    catv_rating: str = None
    catvfr_rating: str = None
    cbfc_rating: str = None
    ccc_rating: str = None
    cce_rating: str = None
    chfilm_rating: str = None
    chvrs_rating: str = None
    cicf_rating: str = None
    cna_rating: str = None
    cnc_rating: str = None
    csa_rating: str = None
    cscf_rating: str = None
    czfilm_rating: str = None
    djctq_rating: str = None
    djctq_rating_reasons: list[str] = None
    ecbmct_rating: str = None
    eefilm_rating: str = None
    egfilm_rating: str = None
    eirin_rating: str = None
    fcbm_rating: str = None
    fco_rating: str = None
    fmoc_rating: str = None
    fpb_rating: str = None
    fbp_rating_reasons: list[str] = None
    fsk_rating: str = None
    grfilm_rating: str = None
    icaa_rating: str = None
    ifco_rating: str = None
    ilfilm_rating: str = None
    incaa_rating: str = None
    kfcb_rating: str = None
    kijkwijzer_rating: str = None
    kmrb_rating: str = None
    lsf_rating: str = None
    mccaa_rating: str = None
    mccyp_rating: str = None
    mcst_rating: str = None
    mda_rating: str = None
    medietilsynet_rating: str = None
    meku_rating: str = None
    mibac_rating: str = None
    moc_rating: str = None
    moctw_rating: str = None
    mpaa_rating: str = None
    mpaat_rating: str = None
    mtrcb_rating: str = None
    nbc_rating: str = None
    nbcpl_rating: str = None
    nfrc_rating: str = None
    nfvcb_rating: str = None
    nkclv_rating: str = None
    oflc_rating: str = None
    pefilm_rating: str = None
    rcnof_rating: str = None
    resorteviolencia_rating: str = None
    rtc_rating: str = None
    rte_rating: str = None
    russia_rating: str = None
    skfilm_rating: str = None
    smais_rating: str = None
    smsa_rating: str = None
    tvpg_rating: str = None
    yt_rating: str = None

@dataclass # top-level
class ContentDetails:
    duration: str = None
    dimension: str = None
    definition: str = None
    caption: str = None
    licensed_content: bool = None
    content_rating: ContentRating = None
    projection: str = None
    has_custom_thumbnails: bool = None

@dataclass # top-level
class Status:
    upload_status: str = None 
    failure_reason: str = None 
    rejection_reason: str = None 
    privacy_status: str = None 
    publish_at: str = None
    license: str = None
    embeddable: bool = None 
    public_stats_viewable: bool = None 
    made_for_kids: bool = None 
    self_declared_made_for_kid: bool = None
    
@dataclass # top-level
class Statistics:
    view_count: int = None
    like_count: int = None
    dislike_count: int = None
    favorite_count: int = None
    comment_count: int = None
    
@dataclass # top-level
class Player:
    embed_html: str = None
    embed_height: int = None
    embed_width: int = None
    
@dataclass # top-level
class TopicDetails:
    topic_ids: list[str] = None
    relevant_topic_ids: list[str] = None
    topic_categories: list[str] = None
    
@dataclass # top-level
class RecordingDetails:
    recording_date: str = None

@dataclass
class VideoStream:
    width_pixels: int = None
    height_pixels: int = None
    frame_rate_fps: int = None 
    aspect_ratio: int = None 
    codec: str = None 
    bitrate_bps: int = None  
    rotation: str = None 
    vendor: str = None 

@dataclass
class AudioStream:
    channel_count: int = None
    codec: str = None 
    bitrate_bps: int = None
    vendor: str = None
    
@dataclass # top-level
class FileDetails:
    file_name: str = None 
    file_size: int = None 
    file_type: str = None 
    container: str = None 
    duration_ms: int = None  
    bitrate_bps: int = None  
    creation_time: str = None
    video_streams: list[VideoStream] = None
    audio_streams: list[AudioStream] = None

@dataclass
class ProcessingProgress:
    parts_total: int = None
    parts_processed: int = None
    time_left_ms: int = None
    
@dataclass # top-level
class ProcessingDetails:
    processing_status: str = None
    processing_failure_reason: str = None
    file_details_availability: str = None
    processing_issues_availability: str = None
    tag_suggestions_availability: str = None
    editor_suggestions_availability: str = None
    thumbnails_availability: str = None
    processing_progress: ProcessingProgress = None

@dataclass # top-level
class LivestreamingDetails:
    actual_start_time: str = None
    actual_end_time: str = None
    scheduled_start_time: str = None
    scheduled_end_time: str = None
    concurrent_viewers: int = None 
    active_live_chat_id: str = None

@dataclass 
class TagSuggestions:
    tag: str = None
    category_restricts: list[str] = None
    
@dataclass # top-level
class Suggestions:
    processing_errors: list[str] = None
    processing_warnings: list[str] = None
    processing_hints: list[str] = None
    editor_suggestions: list[str] = None
    tag_suggestions: list[TagSuggestions] = None

@dataclass
class VideoResource:
    """
    The class representation for the `Video` JSON resource during request bodies and responses.
    """    
    id: str = None
    kind: str = "youtube#video"
    etag: str = None
    snippet: Snippet = Snippet()
    status: Status = Status()
    recording_details: RecordingDetails = RecordingDetails()
        
    content_details: ContentDetails = None
    file_details: FileDetails = None
    live_streaming_details: LivestreamingDetails = None
    processing_details: ProcessingDetails = None
    topic_details: TopicDetails = None
    player: Player = None
    statistics: Statistics = None
    suggestions: Suggestions = None
    
    @classmethod
    def _from_resource_dict(cls, resource: dict):
        """
        Creates a resource from a returned resource dictionary.
        """
        inst = assign_resource_dict_to_class(resource, cls)
        return inst
    
nyaa = {
            "kind": "youtube#video",
            "etag": "x67Tv9bXQNH85HJyeMQw1_TfJ9E",
            "id": "BwodfmqvkCA",
            "snippet": {
                "publishedAt": "2022-01-24T08:14:00Z",
                "channelId": "UCCXX6ZVbhusEhEb-AQF4qTg",
                "title": "tfw",
                "description": "",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/BwodfmqvkCA/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/BwodfmqvkCA/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/BwodfmqvkCA/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    },
                    "standard": {
                        "url": "https://i.ytimg.com/vi/BwodfmqvkCA/sddefault.jpg",
                        "width": 640,
                        "height": 480
                    }
                },
                "channelTitle": "iwanttodie",
                "categoryId": "22",
                "liveBroadcastContent": "none",
                "localized": {
                    "title": "tfw",
                    "description": ""
                }
            },
            "contentDetails": {
                "duration": "PT44S",
                "dimension": "2d",
                "definition": "sd",
                "caption": "false",
                "licensedContent": False,
                "contentRating": {},
                "projection": "rectangular",
                "hasCustomThumbnail": False
            },
            "statistics": {
                "viewCount": "0",
                "likeCount": "0",
                "dislikeCount": "0",
                "favoriteCount": "0",
                "commentCount": "0"
            },
            "fileDetails": {
                "fileName": "redditsave.com_blade_sorcery_extremely_professional_stealth_kill-xy6fu3a9z0a81-480.mp4",
                "fileType": "video",
                "container": "mov",
                "videoStreams": [
                    {
                        "widthPixels": 854,
                        "heightPixels": 480,
                        "frameRateFps": 30,
                        "aspectRatio": 1.7769784152732992,
                        "codec": "h264",
                        "bitrateBps": "1019482"
                    }
                ],
                "audioStreams": [
                    {
                        "channelCount": 2,
                        "codec": "aac",
                        "bitrateBps": "154234"
                    }
                ],
                "durationMs": "43300",
                "bitrateBps": "1173716"
            },
            "processingDetails": {
                "processingStatus": "succeeded",
                "fileDetailsAvailability": "available",
                "processingIssuesAvailability": "available",
                "tagSuggestionsAvailability": "inProgress",
                "editorSuggestionsAvailability": "inProgress",
                "thumbnailsAvailability": "available"
            },
            "suggestions": {
                "processingHints": [
                    "nonStreamableMov"
                ]
            }
        }

bruh = VideoResource._from_resource_dict(nyaa)
print(bruh.file_details)
print(bruh.snippet)
# print(bruh.statistics)